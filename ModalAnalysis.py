def ModalAnalysis(numEigen, pflag=0, outname=None):
    """
    Details
    -------
        This script will return the modal properties of an OpenSeespy model.
    
    Information
    -----------
        Author: Volkan Ozsarac, Earthquake Engineering PhD Candidate
        Affiliation: University School for Advanced Studies IUSS Pavia
        e-mail: volkanozsarac@iusspavia.it
    
    References
    ----------
        Chopra, A.K. 2012. Dynamics of Structures: Theory and 
        Applications to Earthquake Engineering, Prentice Hall.
    Notes
    -----
        Total (activated) mass is obtained by summing the masses assigned to the
        unrestrained degrees of freedoms (DOFs). Thus, it should not be confused 
        with total mass assigned to all DOFs. Influence vectors for rotational 
        excitation are not correct at the moment, this addition remains as future work.
        Which reference point to use is not clear for rotational excitations.
        SAP2000 and Seismostruct use different reference points.
        
    Parameters
    ----------
    numEigen : int
        Number of eigenvalues to calculate.
    pflag    : int (1 or 0)
        flag to print output information on screen
    outname  : str, optional (The default is None)
        if not None and pFlag==1, the modal properties for the 
        first numEigen modes will be writtend into outname.csv.
    Returns
    -------
    T        : numpy.ndarray
        Period array for the first numEigen modes.
    Mratios  : dictionary
        Effective modal mass participation ratios for the first numEigen modes.
    Mfactors : dictionary
        Modal particpation factors for the first numEigen modes.
    Mtots    : dictionary
        Total activated masses.
    """
    import numpy as np
    import openseespy.opensees as op
    import sys
    op.wipeAnalysis()
    # op.constraints('Transformation')
    # op.numberer('RCM')
    # op.system('BandGeneral')
    # op.test('NormDispIncr', 1.0e-7, 50)  # determine if convergence has been achieved at the end of an iteration step
    # op.algorithm('KrylovNewton')  # use Newton solution algorithm: updates tangent stiffness at every iteration
    # # op.integrator('Newmark', 0.5, 0.25)
    # op.analysis('Transient')

    # op.constraints('Transformation')
    # op.numberer("Plain")
    # op.system('FullGeneral')
    # op.algorithm('Linear')
    # op.analysis('Transient')

    op.system('FullGeneral')
    op.analysis('Transient')

    # Extract the Mass Matrix
    # Note that this is not the global mass matrix, but unrestrained part (Muu)

    op.integrator('GimmeMCK', 1.0, 0.0, 0.0)
    op.analyze(1, 0.0)
    # Number of equations in the model
    N = op.systemSize()  # Has to be done after analyze
    Mmatrix = op.printA('-ret')  # Or use op.printA('-file','M.out')
    Mmatrix = np.array(Mmatrix)  # Convert the list to an array
    Mmatrix.shape = (N, N)  # Make the array an NxN matrix
    # print('\n************************************************************',
    #       '\nExtracting the mass matrix, ignore the warnings...')

    # Determine maximum number of DOFs/node used in the system
    NDF = 0
    for node in op.getNodeTags():
        temp = len(op.nodeDOFs(node))
        if temp > NDF: NDF = temp

    DOFs = []  # List containing indices of unrestrained DOFs
    used = {}  # Dictionary with nodes and associated unrestrained DOFs
    ldict = {}  # Dictionary containing influence vectors
    Mratios = {}  # Dictionary containing effective modal masses ratios
    Mfactors = {}  # Dictionary containing modal participation factors
    for i in range(1, NDF + 1):
        ldict[i] = np.zeros([N, 1])
        Mratios[i] = np.zeros(numEigen)
        Mfactors[i] = np.zeros(numEigen)

    # Create the influence vectors, and get the unrestrained DOFs assigned to the nodes
    # TODO -1: The influence vectors are not correct in case of rotational excitations
    # One typical approach is to use center of mass on plane
    idx = 0  # Counter for unrestrained DOFs
    for node in op.getNodeTags():  # Start iterating over each node
        used[node] = []  # Unrestrain local DOF ids
        ndof = len(op.nodeDOFs(node))  # Total number of DOFs assigned
        for j in range(ndof):  # Iterate over each DOF
            temp = op.nodeDOFs(node)[j]  # Get the global DOF id (-1 if restrained)
            if temp not in DOFs and temp >= 0:  # Check if this DOF is unrestrained and is not known before
                DOFs.append(temp)  # Save the global id of DOF
                used[node].append(j + 1)  # Save the local id of DOF
                ldict[j + 1][idx, 0] = 1  # Influence vectors for horizontal and vertical excitations
                idx += 1  # Increase the counter

    # This does not seem necessary when numberer is "Plain"
    # But lets reorganize the mass matrix anyway
    Mmatrix = Mmatrix[DOFs, :][:, DOFs]

    # Calculate the total masses assigned to the unrestrained DOFs
    Mtots = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(1, NDF + 1):
        Mtots[i] = (ldict[i].T @ Mmatrix @ ldict[i])[0, 0]

    # Perform eigenvalue analysis
    op.wipeAnalysis()
    listSolvers = ['-genBandArpack', '-fullGenLapack', '-symmBandLapack']
    ok = 1
    for s in listSolvers:
        # print("Using %s as solver..." % s[1:])
        try:
            eigenValues = op.eigen(s, numEigen)
            catchOK = 0
            ok = 0
        except:
            catchOK = 1

        if catchOK == 0:
            for i in range(numEigen):
                if eigenValues[i] < 0:
                    ok = 1
            if ok == 0:
                # print('Eigenvalue analysis is completed.')
                break
    if ok != 0:
        # print("Error on eigenvalue something is wrong...")
        sys.exit()
    else:
        Lambda = np.asarray(eigenValues)
        Omega = Lambda ** 0.5
        T = 2 * np.pi / Omega
        frq = 1 / T

    # Note: influence factors for rotational excitation is wrong! 
    # Obtain modal properties
    for mode in range(1, numEigen + 1):
        idx = 0
        phi = np.zeros([N, 1])  # Eigen vector
        for node in used:
            for dof in used[node]:
                phi[idx, 0] = op.nodeEigenvector(node, mode, dof)
                idx += 1

        phi = phi / (phi.T @ Mmatrix @ phi) ** 0.5  # Normalize the eigen vector by modal mass
        Mn = phi.T @ Mmatrix @ phi  # Modal mass (should always be equal to 1)

        for j in range(1, NDF + 1):
            if Mtots[j] != 0:  # Check if any mass is assigned
                Ln = phi.T @ Mmatrix @ ldict[j]  # Modal excitation factor
                Mnstar = (Ln ** 2 / Mn)[0, 0]  # Effective modal mass
                Mfactors[j][mode - 1] = Ln / Mn  # Modal participation factor
                Mratios[j][mode - 1] = (Mnstar / Mtots[j] * 100)  # Effective modal mass participation ratio [%]

    for j in range(1, 7):
        try:
            Mratios[j]
        except:
            Mratios[j] = np.zeros(numEigen)
            Mfactors[j] = np.zeros(numEigen)

    # TODO-1: Results are not correct for rotational excitation cases, for now ignore those.
    del Mratios[6], Mratios[5], Mratios[4]
    del Mfactors[6], Mfactors[5], Mfactors[4]

    # Calculate cumulative modal mass participation ratio
    sM1 = np.cumsum(Mratios[1])
    sM2 = np.cumsum(Mratios[2])
    sM3 = np.cumsum(Mratios[3])

    # Print modal analysis results
    if pflag == 1:
        arguments = []
        arguments.append('Modal Periods and Frequencies')
        arguments.append('%4s|%8s|%10s|%12s|%12s' \
                         % ('Mode', 'T [sec]', 'f [Hz]', '\u03C9 [rad/sec]', '\u03BB [rad\u00b2/sec\u00b2]'))
        for mode in range(numEigen):
            arguments.append('%4s|%8s|%10s|%12s|%12s' \
                             % ("{:.0f}".format(mode + 1), "{:.4f}".format(T[mode]), "{:.3f}".format(frq[mode]),
                                "{:.2f}".format(Omega[mode]), "{:.2f}".format(Lambda[mode])))
        arguments.append('Total Activated Masses')
        arguments.append('%8s|%8s|%8s' \
                         % ('M\u2081', 'M\u2082', 'M\u2083'))
        arguments.append('%8s|%8s|%8s' \
                         % ("{:.2f}".format(Mtots[1]), "{:.2f}".format(Mtots[2]), "{:.2f}".format(Mtots[3])))
        arguments.append('Modal Mass Participation Factors')
        arguments.append('%4s|%7s|%7s|%7s' \
                         % ('Mode', '\u0393\u2081', '\u0393\u2082', '\u0393\u2083'))
        for mode in range(numEigen):
            arguments.append('%4s|%7s|%7s|%7s' % ("{:.0f}".format(mode + 1),
                                                  "{:.3f}".format(Mfactors[1][mode]),
                                                  "{:.3f}".format(Mfactors[2][mode]),
                                                  "{:.3f}".format(Mfactors[3][mode])))
        arguments.append('Effective Modal Mass Participation Ratios [%]')
        arguments.append('%4s|%7s|%7s|%7s' \
                         % ('Mode', 'U\u2081', 'U\u2082', 'U\u2083'))
        for mode in range(numEigen):
            arguments.append('%4s|%7s|%7s|%7s' % ("{:.0f}".format(mode + 1), "{:.3f}".format(Mratios[1][mode]),
                                                  "{:.3f}".format(Mratios[2][mode]),
                                                  "{:.3f}".format(Mratios[3][mode])))
        arguments.append('Cumulative Effective Modal Mass Participation Ratios [%]')
        arguments.append('%4s|%7s|%7s|%7s' \
                         % ('Mode', '\u2211U\u2081', '\u2211U\u2082', '\u2211U\u2083'))
        for mode in range(numEigen):
            arguments.append('%4s|%7s|%7s|%7s' % ("{:.0f}".format(mode + 1),
                                                  "{:.3f}".format(sM1[mode]), "{:.3f}".format(sM2[mode]),
                                                  "{:.3f}".format(sM3[mode])))

        # To the screen
        arguments = '\n'.join(arguments)
        # print(arguments)

        # To the .csv file
        if outname != None:
            with open(outname + '.csv', 'w', encoding='utf-32') as f:
                f.write(arguments)

    # print("Modal analysis Done!")
    op.wipeAnalysis()

    return T, Mratios, Mfactors, Mtots
