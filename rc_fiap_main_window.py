��#   - * -   c o d i n g :   u t f - 8   - * - 
 
 
 
 #   F o r m   i m p l e m e n t a t i o n   g e n e r a t e d   f r o m   r e a d i n g   u i   f i l e   ' . \ r c _ f i a p _ m a i n _ w i n d o w . u i ' 
 
 # 
 
 #   C r e a t e d   b y :   P y Q t 5   U I   c o d e   g e n e r a t o r   5 . 1 5 . 1 0 
 
 # 
 
 #   W A R N I N G :   A n y   m a n u a l   c h a n g e s   m a d e   t o   t h i s   f i l e   w i l l   b e   l o s t   w h e n   p y u i c 5   i s 
 
 #   r u n   a g a i n .     D o   n o t   e d i t   t h i s   f i l e   u n l e s s   y o u   k n o w   w h a t   y o u   a r e   d o i n g . 
 
 
 
 
 
 f r o m   P y Q t 5   i m p o r t   Q t C o r e ,   Q t G u i ,   Q t W i d g e t s 
 
 
 
 
 
 c l a s s   U i _ N o n L i n e a r M a i n W i n d o w ( o b j e c t ) : 
 
         d e f   s e t u p U i ( s e l f ,   N o n L i n e a r M a i n W i n d o w ) : 
 
                 N o n L i n e a r M a i n W i n d o w . s e t O b j e c t N a m e ( " N o n L i n e a r M a i n W i n d o w " ) 
 
                 N o n L i n e a r M a i n W i n d o w . r e s i z e ( 2 5 5 1 ,   1 3 5 2 ) 
 
                 s e l f . c e n t r a l w i d g e t   =   Q t W i d g e t s . Q W i d g e t ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . c e n t r a l w i d g e t . s e t O b j e c t N a m e ( " c e n t r a l w i d g e t " ) 
 
                 s e l f . g r i d L a y o u t   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . c e n t r a l w i d g e t ) 
 
                 s e l f . g r i d L a y o u t . s e t O b j e c t N a m e ( " g r i d L a y o u t " ) 
 
                 s e l f . l a y _ s e c c i o n e s   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ s e c c i o n e s . s e t S p a c i n g ( 7 ) 
 
                 s e l f . l a y _ s e c c i o n e s . s e t O b j e c t N a m e ( " l a y _ s e c c i o n e s " ) 
 
                 s e l f . l b l _ e n c a b e z a d o   =   Q t W i d g e t s . Q L a b e l ( s e l f . c e n t r a l w i d g e t ) 
 
                 s e l f . l b l _ e n c a b e z a d o . s e t T e x t ( " " ) 
 
                 s e l f . l b l _ e n c a b e z a d o . s e t P i x m a p ( Q t G u i . Q P i x m a p ( " . \ \ b a n n e r . j p g " ) ) 
 
                 s e l f . l b l _ e n c a b e z a d o . s e t O b j e c t N a m e ( " l b l _ e n c a b e z a d o " ) 
 
                 s e l f . l a y _ s e c c i o n e s . a d d W i d g e t ( s e l f . l b l _ e n c a b e z a d o ) 
 
                 s e l f . l a y _ p r i n c i p a l   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ p r i n c i p a l . s e t O b j e c t N a m e ( " l a y _ p r i n c i p a l " ) 
 
                 s e l f . t w d _ p r i n c i p a l   =   Q t W i d g e t s . Q T a b W i d g e t ( s e l f . c e n t r a l w i d g e t ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t O b j e c t N a m e ( " t w d _ p r i n c i p a l " ) 
 
                 s e l f . t a b _ f r a m e _ d a t a   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ f r a m e _ d a t a . s e t O b j e c t N a m e ( " t a b _ f r a m e _ d a t a " ) 
 
                 s e l f . g r i d L a y o u t _ 4   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g r i d L a y o u t _ 4 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 " ) 
 
                 s e l f . l a y _ f r a m e _ d a t a   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f r a m e _ d a t a . s e t O b j e c t N a m e ( " l a y _ f r a m e _ d a t a " ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 1   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 1 . s e t O b j e c t N a m e ( " l a y _ f o r m _ d a t a _ r o w _ 1 " ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s . s e t O b j e c t N a m e ( " g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s " ) 
 
                 s e l f . g r i d L a y o u t _ 5   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s ) 
 
                 s e l f . g r i d L a y o u t _ 5 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 5 " ) 
 
                 s e l f . l a y _ c o l u m n s _ s e c t i o n s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ c o l u m n s _ s e c t i o n s . s e t O b j e c t N a m e ( " l a y _ c o l u m n s _ s e c t i o n s " ) 
 
                 s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s ) 
 
                 s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t O b j e c t N a m e ( " g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r " ) 
 
                 s e l f . g r i d L a y o u t _ 6   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ) 
 
                 s e l f . g r i d L a y o u t _ 6 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 6 " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t O b j e c t N a m e ( " f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r " ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ w i d t h   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ w i d t h . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ s e c t i o n s _ w i d t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ c o l u m n s _ s e c t i o n s _ w i d t h ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ w i d t h   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ w i d t h . s e t O b j e c t N a m e ( " s p x _ c o l u m n s _ s e c t i o n s _ w i d t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ c o l u m n s _ s e c t i o n s _ w i d t h ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ d e p t h   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ d e p t h . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ s e c t i o n s _ d e p t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ c o l u m n s _ s e c t i o n s _ d e p t h ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ d e p t h   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ d e p t h . s e t O b j e c t N a m e ( " s p x _ c o l u m n s _ s e c t i o n s _ d e p t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ c o l u m n s _ s e c t i o n s _ d e p t h ) 
 
                 s e l f . g r i d L a y o u t _ 6 . a d d L a y o u t ( s e l f . f r m _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ c o l u m n s _ s e c t i o n s . a d d W i d g e t ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r ) 
 
                 s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s ) 
 
                 s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t O b j e c t N a m e ( " g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r " ) 
 
                 s e l f . g r i d L a y o u t _ 2   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ) 
 
                 s e l f . g r i d L a y o u t _ 2 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t O b j e c t N a m e ( " f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r " ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h . s e t O b j e c t N a m e ( " s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ) 
 
                 s e l f . s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h . s e t O b j e c t N a m e ( " s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h " ) 
 
                 s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h ) 
 
                 s e l f . g r i d L a y o u t _ 2 . a d d L a y o u t ( s e l f . f r m _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ c o l u m n s _ s e c t i o n s . a d d W i d g e t ( s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r ) 
 
                 s e l f . g r i d L a y o u t _ 5 . a d d L a y o u t ( s e l f . l a y _ c o l u m n s _ s e c t i o n s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 1 . a d d W i d g e t ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s . s e t O b j e c t N a m e ( " g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s " ) 
 
                 s e l f . g r i d L a y o u t _ 7   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s ) 
 
                 s e l f . g r i d L a y o u t _ 7 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 7 " ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s . s e t C o n t e n t s M a r g i n s ( - 1 ,   2 9 ,   - 1 ,   - 1 ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s . s e t O b j e c t N a m e ( " f r m _ b e a m s _ s e c t i o n s " ) 
 
                 s e l f . l b l _ b e a m _ s e c t i o n s _ w i d t h   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s ) 
 
                 s e l f . l b l _ b e a m _ s e c t i o n s _ w i d t h . s e t O b j e c t N a m e ( " l b l _ b e a m _ s e c t i o n s _ w i d t h " ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ b e a m _ s e c t i o n s _ w i d t h ) 
 
                 s e l f . s p x _ b e a m _ s e c t i o n s _ w i d t h   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s ) 
 
                 s e l f . s p x _ b e a m _ s e c t i o n s _ w i d t h . s e t O b j e c t N a m e ( " s p x _ b e a m _ s e c t i o n s _ w i d t h " ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ b e a m _ s e c t i o n s _ w i d t h ) 
 
                 s e l f . l b l _ b e a m _ s e c t i o n s _ d e p t h   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s ) 
 
                 s e l f . l b l _ b e a m _ s e c t i o n s _ d e p t h . s e t O b j e c t N a m e ( " l b l _ b e a m _ s e c t i o n s _ d e p t h " ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ b e a m _ s e c t i o n s _ d e p t h ) 
 
                 s e l f . s p x _ b e a m _ s e c t i o n s _ d e p t h   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s ) 
 
                 s e l f . s p x _ b e a m _ s e c t i o n s _ d e p t h . s e t O b j e c t N a m e ( " s p x _ b e a m _ s e c t i o n s _ d e p t h " ) 
 
                 s e l f . f r m _ b e a m s _ s e c t i o n s . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ b e a m _ s e c t i o n s _ d e p t h ) 
 
                 s e l f . g r i d L a y o u t _ 7 . a d d L a y o u t ( s e l f . f r m _ b e a m s _ s e c t i o n s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 1 . a d d W i d g e t ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d . s e t O b j e c t N a m e ( " g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d " ) 
 
                 s e l f . g r i d L a y o u t _ 8   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . g r i d L a y o u t _ 8 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 8 " ) 
 
                 s e l f . f r m _ s e i s m i c _ l o a d   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ s e i s m i c _ l o a d . s e t C o n t e n t s M a r g i n s ( - 1 ,   2 9 ,   - 1 ,   - 1 ) 
 
                 s e l f . f r m _ s e i s m i c _ l o a d . s e t O b j e c t N a m e ( " f r m _ s e i s m i c _ l o a d " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . s e t S i z e C o n s t r a i n t ( Q t W i d g e t s . Q L a y o u t . S e t D e f a u l t C o n s t r a i n t ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . s e t S p a c i n g ( 6 ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . s e t O b j e c t N a m e ( " l a y _ s e i s m i c _ l o a d " ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ r   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ r . s e t O b j e c t N a m e ( " l b l _ s e i s m i c _ l o a d _ r " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . l b l _ s e i s m i c _ l o a d _ r ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ r   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ r . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n L e a d i n g | Q t C o r e . Q t . A l i g n L e f t | Q t C o r e . Q t . A l i g n V C e n t e r ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ r . s e t O b j e c t N a m e ( " s p x _ s e i s m i c _ l o a d _ r " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . s p x _ s e i s m i c _ l o a d _ r ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ c d   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ c d . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n R i g h t | Q t C o r e . Q t . A l i g n T r a i l i n g | Q t C o r e . Q t . A l i g n V C e n t e r ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ c d . s e t O b j e c t N a m e ( " l b l _ s e i s m i c _ l o a d _ c d " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . l b l _ s e i s m i c _ l o a d _ c d ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ c d   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ c d . s e t O b j e c t N a m e ( " s p x _ s e i s m i c _ l o a d _ c d " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . s p x _ s e i s m i c _ l o a d _ c d ) 
 
                 s e l f . l b l _ _ s e i s m i c _ l o a d _ o m e g a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . l b l _ _ s e i s m i c _ l o a d _ o m e g a . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n R i g h t | Q t C o r e . Q t . A l i g n T r a i l i n g | Q t C o r e . Q t . A l i g n V C e n t e r ) 
 
                 s e l f . l b l _ _ s e i s m i c _ l o a d _ o m e g a . s e t O b j e c t N a m e ( " l b l _ _ s e i s m i c _ l o a d _ o m e g a " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . l b l _ _ s e i s m i c _ l o a d _ o m e g a ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ o m e g a   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ o m e g a . s e t O b j e c t N a m e ( " s p x _ s e i s m i c _ l o a d _ o m e g a " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . s p x _ s e i s m i c _ l o a d _ o m e g a ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ i   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ i . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n R i g h t | Q t C o r e . Q t . A l i g n T r a i l i n g | Q t C o r e . Q t . A l i g n V C e n t e r ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ i . s e t O b j e c t N a m e ( " l b l _ s e i s m i c _ l o a d _ i " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . l b l _ s e i s m i c _ l o a d _ i ) 
 
                 s e l f . s p x _ _ s e i s m i c _ l o a d _ i   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . s p x _ _ s e i s m i c _ l o a d _ i . s e t O b j e c t N a m e ( " s p x _ _ s e i s m i c _ l o a d _ i " ) 
 
                 s e l f . l a y _ s e i s m i c _ l o a d . a d d W i d g e t ( s e l f . s p x _ _ s e i s m i c _ l o a d _ i ) 
 
                 s e l f . f r m _ s e i s m i c _ l o a d . s e t L a y o u t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l a y _ s e i s m i c _ l o a d ) 
 
                 s e l f . g r i d L a y o u t _ 8 . a d d L a y o u t ( s e l f . f r m _ s e i s m i c _ l o a d ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 1 . a d d W i d g e t ( s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d ) 
 
                 s e l f . g b x _ t y p e _ l o a d   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ t y p e _ l o a d . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n L e a d i n g | Q t C o r e . Q t . A l i g n L e f t | Q t C o r e . Q t . A l i g n T o p ) 
 
                 s e l f . g b x _ t y p e _ l o a d . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d " ) 
 
                 s e l f . g r i d L a y o u t _ 9   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s e l f . g r i d L a y o u t _ 9 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 9 " ) 
 
                 s e l f . f r m _ t y p e _ l o a d   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t C o n t e n t s M a r g i n s ( - 1 ,   2 9 ,   - 1 ,   - 1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t O b j e c t N a m e ( " f r m _ t y p e _ l o a d " ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d " ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t O b j e c t N a m e ( " c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d " ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . a d d I t e m ( " " ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . a d d I t e m ( " " ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . a d d I t e m ( " " ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . a d d I t e m ( " " ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . a d d I t e m ( " " ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . a d d I t e m ( " " ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r " ) 
 
                 s e l f . g r i d L a y o u t _ 1 7   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r ) 
 
                 s e l f . g r i d L a y o u t _ 1 7 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 7 " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s e t O b j e c t N a m e ( " f r m _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r " ) 
 
                 s e l f . t x t _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ t e x t _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . F i x e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . t x t _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ t e x t _ f i l e . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . t x t _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ t e x t _ f i l e . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . t x t _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ t e x t _ f i l e . s e t O b j e c t N a m e ( " t x t _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ t e x t _ f i l e " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ t e x t _ f i l e ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ s p e c t _ t e x t _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ s p e c t _ t e x t _ f i l e . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ s p e c t _ t e x t _ f i l e " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ s p e c t _ t e x t _ f i l e ) 
 
                 s e l f . g r i d L a y o u t _ 1 7 . a d d L a y o u t ( s e l f . f r m _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 . s e t E n a b l e d ( T r u e ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 . s e t S t y l e S h e e t ( " " ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ a s c e _ 7 " ) 
 
                 s e l f . g r i d L a y o u t _ 1 2   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s e l f . g r i d L a y o u t _ 1 2 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 2 " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t O b j e c t N a m e ( " l a y _ t y p e _ l o a d _ a s c e _ 7 " ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d s . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d s " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d s ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . F i x e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d s . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d s . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d s . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d s " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d s ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d 1   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d 1   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . F i x e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ t l   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ t l . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ a s c e _ 7 _ t l " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ t l ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ t l   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . F i x e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ t l . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ t l . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ t l . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ a s c e _ 7 _ t l " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ a s c e _ 7 _ t l ) 
 
                 s e l f . g r i d L a y o u t _ 1 2 . a d d L a y o u t ( s e l f . l a y _ t y p e _ l o a d _ a s c e _ 7 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 1 0   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ n s r 1 0 " ) 
 
                 s e l f . g r i d L a y o u t _ 1 3   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 ) 
 
                 s e l f . g r i d L a y o u t _ 1 3 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 3 " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ n s r 1 0   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ n s r 1 0 . s e t O b j e c t N a m e ( " l a y _ t y p e _ l o a d _ n s r 1 0 " ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a a . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ n s r 1 0 _ a a " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ n s r 1 0 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a a ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ n s r 1 0 _ a a   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ n s r 1 0 _ a a . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ n s r 1 0 _ a a " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ n s r 1 0 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ n s r 1 0 _ a a ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a v   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a v . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ n s r 1 0 _ a v " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ n s r 1 0 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a v ) 
 
                 s e l f . s p x _ _ t y p e _ l o a d _ n s r 1 0 _ a v   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 ) 
 
                 s e l f . s p x _ _ t y p e _ l o a d _ n s r 1 0 _ a v . s e t O b j e c t N a m e ( " s p x _ _ t y p e _ l o a d _ n s r 1 0 _ a v " ) 
 
                 s e l f . l a y _ t y p e _ l o a d _ n s r 1 0 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ _ t y p e _ l o a d _ n s r 1 0 _ a v ) 
 
                 s e l f . g r i d L a y o u t _ 1 3 . a d d L a y o u t ( s e l f . l a y _ t y p e _ l o a d _ n s r 1 0 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ n s r 9 8 " ) 
 
                 s e l f . g r i d L a y o u t _ 1 4   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 ) 
 
                 s e l f . g r i d L a y o u t _ 1 4 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 4 " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ n s r 9 8   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ n s r 9 8 . s e t O b j e c t N a m e ( " f r m _ t y p e _ l o a d _ n s r 9 8 " ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ a a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ a a . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ n s r 9 8 _ a a " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ n s r 9 8 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ a a ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 _ a a   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 _ a a . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ n s r 9 8 _ a a " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ n s r 9 8 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 _ a a ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ s . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ n s r 9 8 _ s " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ n s r 9 8 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ s ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 _ s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 _ s . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ n s r 9 8 _ s " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ n s r 9 8 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 _ s ) 
 
                 s e l f . g r i d L a y o u t _ 1 4 . a d d L a y o u t ( s e l f . f r m _ t y p e _ l o a d _ n s r 9 8 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 . s e t O b j e c t N a m e ( " g b x _ t y p e _ l o a d _ c c c s r 8 4 " ) 
 
                 s e l f . g r i d L a y o u t _ 1 5   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . g r i d L a y o u t _ 1 5 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 5 " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t O b j e c t N a m e ( " f r m _ t y p e _ l o a d _ c c c s r 8 4 " ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a a . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a a " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a a ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a a   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a a . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a a " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a a ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a v   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a v . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a v " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a v ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a v   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a v . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a v " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ a v ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ s . s e t O b j e c t N a m e ( " l b l _ t y p e _ l o a d _ c c c s r 8 4 _ s " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ s ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ s . s e t O b j e c t N a m e ( " s p x _ t y p e _ l o a d _ c c c s r 8 4 _ s " ) 
 
                 s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t y p e _ l o a d _ c c c s r 8 4 _ s ) 
 
                 s e l f . g r i d L a y o u t _ 1 5 . a d d L a y o u t ( s e l f . f r m _ t y p e _ l o a d _ c c c s r 8 4 ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 ) 
 
                 s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e . s e t O b j e c t N a m e ( " g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e " ) 
 
                 s e l f . g r i d L a y o u t _ 5 4   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e ) 
 
                 s e l f . g r i d L a y o u t _ 5 4 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 5 4 " ) 
 
                 s e l f . f o r m L a y o u t _ 6   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f o r m L a y o u t _ 6 . s e t O b j e c t N a m e ( " f o r m L a y o u t _ 6 " ) 
 
                 s e l f . l b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e ) 
 
                 s e l f . l b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e . s e t O b j e c t N a m e ( " l b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e " ) 
 
                 s e l f . f o r m L a y o u t _ 6 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e ) 
 
                 s e l f . s p x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e . s e t O b j e c t N a m e ( " s p x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e " ) 
 
                 s e l f . f o r m L a y o u t _ 6 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e ) 
 
                 s e l f . g r i d L a y o u t _ 5 4 . a d d L a y o u t ( s e l f . f o r m L a y o u t _ 6 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ t y p e _ l o a d . s e t W i d g e t ( 6 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e ) 
 
                 s e l f . g r i d L a y o u t _ 9 . a d d L a y o u t ( s e l f . f r m _ t y p e _ l o a d ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 1 . a d d W i d g e t ( s e l f . g b x _ t y p e _ l o a d ) 
 
                 s e l f . l a y _ f r a m e _ d a t a . a d d L a y o u t ( s e l f . l a y _ f o r m _ d a t a _ r o w _ 1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 2   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 2 . s e t O b j e c t N a m e ( " l a y _ f o r m _ d a t a _ r o w _ 2 " ) 
 
                 s e l f . g b x _ f r a m e _ g e o m e t r y   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f r a m e _ g e o m e t r y . s e t O b j e c t N a m e ( " g b x _ f r a m e _ g e o m e t r y " ) 
 
                 s e l f . g r i d L a y o u t _ 1 0   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f r a m e _ g e o m e t r y ) 
 
                 s e l f . g r i d L a y o u t _ 1 0 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 0 " ) 
 
                 s e l f . f r m _ f r a m e _ g e o m e t r y   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ f r a m e _ g e o m e t r y . s e t O b j e c t N a m e ( " f r m _ f r a m e _ g e o m e t r y " ) 
 
                 s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ g e o m e t r y ) 
 
                 s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y . s e t O b j e c t N a m e ( " l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y " ) 
 
                 s e l f . f r m _ f r a m e _ g e o m e t r y . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y ) 
 
                 s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ f r a m e _ g e o m e t r y ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . F i x e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y . s e t O b j e c t N a m e ( " t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y " ) 
 
                 s e l f . f r m _ f r a m e _ g e o m e t r y . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y ) 
 
                 s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ f r a m e _ g e o m e t r y ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . F i x e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s . s e t O b j e c t N a m e ( " t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s " ) 
 
                 s e l f . f r m _ f r a m e _ g e o m e t r y . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s ) 
 
                 s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ g e o m e t r y ) 
 
                 s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s . s e t O b j e c t N a m e ( " l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s " ) 
 
                 s e l f . f r m _ f r a m e _ g e o m e t r y . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s ) 
 
                 s e l f . g r i d L a y o u t _ 1 0 . a d d L a y o u t ( s e l f . f r m _ f r a m e _ g e o m e t r y ,   0 ,   1 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 2 . a d d W i d g e t ( s e l f . g b x _ f r a m e _ g e o m e t r y ) 
 
                 s e l f . g b x _ f r a m e _ t y p e   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f r a m e _ t y p e . s e t O b j e c t N a m e ( " g b x _ f r a m e _ t y p e " ) 
 
                 s e l f . g r i d L a y o u t _ 1 1   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f r a m e _ t y p e ) 
 
                 s e l f . g r i d L a y o u t _ 1 1 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 1 " ) 
 
                 s e l f . l a y _ f r a m e _ t y p e   =   Q t W i d g e t s . Q G r i d L a y o u t ( ) 
 
                 s e l f . l a y _ f r a m e _ t y p e . s e t O b j e c t N a m e ( " l a y _ f r a m e _ t y p e " ) 
 
                 s e l f . r b n _ f r a m e _ t y p e _ s p a t i a l   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ f r a m e _ t y p e ) 
 
                 s e l f . r b n _ f r a m e _ t y p e _ s p a t i a l . s e t O b j e c t N a m e ( " r b n _ f r a m e _ t y p e _ s p a t i a l " ) 
 
                 s e l f . l a y _ f r a m e _ t y p e . a d d W i d g e t ( s e l f . r b n _ f r a m e _ t y p e _ s p a t i a l ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . r b n _ f r a m e _ t y p e _ p e r i m e t r a l   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ f r a m e _ t y p e ) 
 
                 s e l f . r b n _ f r a m e _ t y p e _ p e r i m e t r a l . s e t O b j e c t N a m e ( " r b n _ f r a m e _ t y p e _ p e r i m e t r a l " ) 
 
                 s e l f . l a y _ f r a m e _ t y p e . a d d W i d g e t ( s e l f . r b n _ f r a m e _ t y p e _ p e r i m e t r a l ,   0 ,   1 ,   1 ,   1 ) 
 
                 s e l f . g r i d L a y o u t _ 1 1 . a d d L a y o u t ( s e l f . l a y _ f r a m e _ t y p e ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 2 . a d d W i d g e t ( s e l f . g b x _ f r a m e _ t y p e ) 
 
                 s e l f . g b x _ f r a m e _ t r i b u t a r y   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f r a m e _ t r i b u t a r y . s e t O b j e c t N a m e ( " g b x _ f r a m e _ t r i b u t a r y " ) 
 
                 s e l f . g r i d L a y o u t _ 1 8   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . g r i d L a y o u t _ 1 8 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 8 " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t O b j e c t N a m e ( " l a y _ f r a m e _ t r i b u t a r y " ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d . s e t O b j e c t N a m e ( " s p x _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d . s e t O b j e c t N a m e ( " s p x _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y . s e t O b j e c t N a m e ( " s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y ) 
 
                 s e l f . l b l _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . l b l _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c . s e t O b j e c t N a m e ( " l b l _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c . s e t O b j e c t N a m e ( " s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ p d e l t a _ l e a n i n g _ c o l u m n   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ p d e l t a _ l e a n i n g _ c o l u m n . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ t r i b u t a r y _ p d e l t a _ l e a n i n g _ c o l u m n " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ p d e l t a _ l e a n i n g _ c o l u m n ) 
 
                 s e l f . l a y _ _ f r a m e _ t r i b u t a r y _ p d e l t a   =   Q t W i d g e t s . Q G r i d L a y o u t ( ) 
 
                 s e l f . l a y _ _ f r a m e _ t r i b u t a r y _ p d e l t a . s e t O b j e c t N a m e ( " l a y _ _ f r a m e _ t r i b u t a r y _ p d e l t a " ) 
 
                 s e l f . r b n _ f r a m e _ t r i b u t a r y _ y e s   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . r b n _ f r a m e _ t r i b u t a r y _ y e s . s e t O b j e c t N a m e ( " r b n _ f r a m e _ t r i b u t a r y _ y e s " ) 
 
                 s e l f . l a y _ _ f r a m e _ t r i b u t a r y _ p d e l t a . a d d W i d g e t ( s e l f . r b n _ f r a m e _ t r i b u t a r y _ y e s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . r b n _ f r a m e _ t r i b u t a r y _ n o   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . r b n _ f r a m e _ t r i b u t a r y _ n o . s e t O b j e c t N a m e ( " r b n _ f r a m e _ t r i b u t a r y _ n o " ) 
 
                 s e l f . l a y _ _ f r a m e _ t r i b u t a r y _ p d e l t a . a d d W i d g e t ( s e l f . r b n _ f r a m e _ t r i b u t a r y _ n o ,   0 ,   1 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t L a y o u t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l a y _ _ f r a m e _ t r i b u t a r y _ p d e l t a ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ i n e r t i a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ i n e r t i a . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ t r i b u t a r y _ i n e r t i a " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ i n e r t i a ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ i n e r t i a   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . s p x _ f r a m e _ t r i b u t a r y _ i n e r t i a . s e t O b j e c t N a m e ( " s p x _ f r a m e _ t r i b u t a r y _ i n e r t i a " ) 
 
                 s e l f . l a y _ f r a m e _ t r i b u t a r y . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ f r a m e _ t r i b u t a r y _ i n e r t i a ) 
 
                 s e l f . g r i d L a y o u t _ 1 8 . a d d L a y o u t ( s e l f . l a y _ f r a m e _ t r i b u t a r y ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 2 . a d d W i d g e t ( s e l f . g b x _ f r a m e _ t r i b u t a r y ) 
 
                 s e l f . g b x _ m e m b e r   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ m e m b e r . s e t O b j e c t N a m e ( " g b x _ m e m b e r " ) 
 
                 s e l f . g r i d L a y o u t _ 2 1   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . g r i d L a y o u t _ 2 1 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 1 " ) 
 
                 s e l f . l a y _ m e m b e r   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . l a y _ m e m b e r . s e t O b j e c t N a m e ( " l a y _ m e m b e r " ) 
 
                 s e l f . l b l _ m e m b e r _ m e m b e r   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . l b l _ m e m b e r _ m e m b e r . s e t O b j e c t N a m e ( " l b l _ m e m b e r _ m e m b e r " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m e m b e r _ m e m b e r ) 
 
                 s e l f . l b l _ m e m b e r _ m o m e n t _ f o r _ i n t e r t i a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . l b l _ m e m b e r _ m o m e n t _ f o r _ i n t e r t i a . s e t O b j e c t N a m e ( " l b l _ m e m b e r _ m o m e n t _ f o r _ i n t e r t i a " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ m e m b e r _ m o m e n t _ f o r _ i n t e r t i a ) 
 
                 s e l f . l b l _ m e m b e r _ c o l u m n s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . l b l _ m e m b e r _ c o l u m n s . s e t O b j e c t N a m e ( " l b l _ m e m b e r _ c o l u m n s " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m e m b e r _ c o l u m n s ) 
 
                 s e l f . s p i n B o x   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . s p i n B o x . s e t O b j e c t N a m e ( " s p i n B o x " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p i n B o x ) 
 
                 s e l f . l b l _ m e m b e r _ b e a m   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . l b l _ m e m b e r _ b e a m . s e t O b j e c t N a m e ( " l b l _ m e m b e r _ b e a m " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m e m b e r _ b e a m ) 
 
                 s e l f . s p x _ m e m b e r _ b e a m   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . s p x _ m e m b e r _ b e a m . s e t O b j e c t N a m e ( " s p x _ m e m b e r _ b e a m " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ m e m b e r _ b e a m ) 
 
                 s e l f . l b l _ m e m b e r _ w a l l s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . l b l _ m e m b e r _ w a l l s . s e t O b j e c t N a m e ( " l b l _ m e m b e r _ w a l l s " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m e m b e r _ w a l l s ) 
 
                 s e l f . s p x _ m e m b e r _ w a l l s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . s p x _ m e m b e r _ w a l l s . s e t O b j e c t N a m e ( " s p x _ m e m b e r _ w a l l s " ) 
 
                 s e l f . l a y _ m e m b e r . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ m e m b e r _ w a l l s ) 
 
                 s e l f . g r i d L a y o u t _ 2 1 . a d d L a y o u t ( s e l f . l a y _ m e m b e r ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 2 . a d d W i d g e t ( s e l f . g b x _ m e m b e r ) 
 
                 s e l f . l a y _ f r a m e _ d a t a . a d d L a y o u t ( s e l f . l a y _ f o r m _ d a t a _ r o w _ 2 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 3   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 3 . s e t O b j e c t N a m e ( " l a y _ f o r m _ d a t a _ r o w _ 3 " ) 
 
                 s e l f . g b x _ m a t e r i a l s   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ m a t e r i a l s . s e t O b j e c t N a m e ( " g b x _ m a t e r i a l s " ) 
 
                 s e l f . g r i d L a y o u t _ 2 0   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . g r i d L a y o u t _ 2 0 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 0 " ) 
 
                 s e l f . f r m _ m a t e r i a l s   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t O b j e c t N a m e ( " f r m _ m a t e r i a l s " ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ l o n g   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ l o n g . s e t O b j e c t N a m e ( " l b l _ m a t e r i a l s _ f _ l o n g " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m a t e r i a l s _ f _ l o n g ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ l o n g   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ l o n g . s e t O b j e c t N a m e ( " s p x _ m a t e r i a l s _ f _ l o n g " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ m a t e r i a l s _ f _ l o n g ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ t r a n s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ t r a n s . s e t O b j e c t N a m e ( " l b l _ m a t e r i a l s _ f _ t r a n s " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m a t e r i a l s _ f _ t r a n s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ t r a n s v   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ t r a n s v . s e t O b j e c t N a m e ( " s p x _ m a t e r i a l s _ f _ t r a n s v " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ m a t e r i a l s _ f _ t r a n s v ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ b e a m s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ b e a m s . s e t O b j e c t N a m e ( " l b l _ m a t e r i a l s _ f _ b e a m s " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ m a t e r i a l s _ f _ b e a m s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ b e a m s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ b e a m s . s e t O b j e c t N a m e ( " s p x _ m a t e r i a l s _ f _ b e a m s " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ m a t e r i a l s _ f _ b e a m s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s _ 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s _ 2 . s e t O b j e c t N a m e ( " s p x _ m a t e r i a l s _ f _ c o l u m n s _ 2 " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s _ 2 ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s . s e t O b j e c t N a m e ( " s p x _ m a t e r i a l s _ f _ c o l u m n s " ) 
 
                 s e l f . f r m _ m a t e r i a l s . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s ) 
 
                 s e l f . g r i d L a y o u t _ 2 0 . a d d L a y o u t ( s e l f . f r m _ m a t e r i a l s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 3 . a d d W i d g e t ( s e l f . g b x _ m a t e r i a l s ) 
 
                 s e l f . g b x _ c o l u m n _ b e a m   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ c o l u m n _ b e a m . s e t O b j e c t N a m e ( " g b x _ c o l u m n _ b e a m " ) 
 
                 s e l f . g r i d L a y o u t _ 2 2   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ c o l u m n _ b e a m ) 
 
                 s e l f . g r i d L a y o u t _ 2 2 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 2 " ) 
 
                 s e l f . f r m _ c o l u m n _ b e a m   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ c o l u m n _ b e a m . s e t O b j e c t N a m e ( " f r m _ c o l u m n _ b e a m " ) 
 
                 s e l f . l b l _ _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n _ b e a m ) 
 
                 s e l f . l b l _ _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n . s e t O b j e c t N a m e ( " l b l _ _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n " ) 
 
                 s e l f . f r m _ c o l u m n _ b e a m . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n ) 
 
                 s e l f . s p x _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ c o l u m n _ b e a m ) 
 
                 s e l f . s p x _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n . s e t O b j e c t N a m e ( " s p x _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n " ) 
 
                 s e l f . f r m _ c o l u m n _ b e a m . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n ) 
 
                 s e l f . g r i d L a y o u t _ 2 2 . a d d L a y o u t ( s e l f . f r m _ c o l u m n _ b e a m ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 3 . a d d W i d g e t ( s e l f . g b x _ c o l u m n _ b e a m ) 
 
                 s e l f . g b x _ f r a m e _ w a l l _ s y s t e m   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ f r a m e _ w a l l _ s y s t e m . s e t O b j e c t N a m e ( " g b x _ f r a m e _ w a l l _ s y s t e m " ) 
 
                 s e l f . g r i d L a y o u t _ 2 3   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . g r i d L a y o u t _ 2 3 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 3 " ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t O b j e c t N a m e ( " f r m _ f r a m e _ w a l l _ s y s t e m " ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s . s e t O b j e c t N a m e ( " l b l _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s " ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s " ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s . s e t O b j e c t N a m e ( " w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s " ) 
 
                 s e l f . g r i d L a y o u t _ 2 4   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s ) 
 
                 s e l f . g r i d L a y o u t _ 2 4 . s e t C o n t e n t s M a r g i n s ( 0 ,   0 ,   0 ,   0 ) 
 
                 s e l f . g r i d L a y o u t _ 2 4 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 4 " ) 
 
                 s e l f . l a y _ _ f r a m e _ w a l l _ s y s t e m _ w a l l s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ _ f r a m e _ w a l l _ s y s t e m _ w a l l s . s e t O b j e c t N a m e ( " l a y _ _ f r a m e _ w a l l _ s y s t e m _ w a l l s " ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 1   =   Q t W i d g e t s . Q L a b e l ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 1 . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n C e n t e r ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 1 . s e t O b j e c t N a m e ( " l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 1 " ) 
 
                 s e l f . l a y _ _ f r a m e _ w a l l _ s y s t e m _ w a l l s . a d d W i d g e t ( s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 1 ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 2 . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n C e n t e r ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 2 . s e t O b j e c t N a m e ( " l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 2 " ) 
 
                 s e l f . l a y _ _ f r a m e _ w a l l _ s y s t e m _ w a l l s . a d d W i d g e t ( s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 2 ) 
 
                 s e l f . g r i d L a y o u t _ 2 4 . a d d L a y o u t ( s e l f . l a y _ _ f r a m e _ w a l l _ s y s t e m _ w a l l s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ w a l l s ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ,   Q t W i d g e t s . Q S i z e P o l i c y . P r e f e r r e d ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n L e a d i n g | Q t C o r e . Q t . A l i g n L e f t | Q t C o r e . Q t . A l i g n V C e n t e r ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w . s e t O b j e c t N a m e ( " l b l _ f r a m e _ w a l l _ s y s t e m _ t w " ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ t w   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ t w . s e t O b j e c t N a m e ( " w g t _ f r a m e _ w a l l _ s y s t e m _ t w " ) 
 
                 s e l f . g r i d L a y o u t _ 2 5   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ t w ) 
 
                 s e l f . g r i d L a y o u t _ 2 5 . s e t C o n t e n t s M a r g i n s ( 0 ,   0 ,   0 ,   0 ) 
 
                 s e l f . g r i d L a y o u t _ 2 5 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 5 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ t w   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ t w . s e t O b j e c t N a m e ( " l a y _ f r a m e _ w a l l _ s y s t e m _ t w " ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 1   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ t w ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 1 . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 1 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ t w . a d d W i d g e t ( s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 1 ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 2   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ t w ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 2 . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 2 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ t w . a d d W i d g e t ( s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ t w _ w a l l 2 ) 
 
                 s e l f . g r i d L a y o u t _ 2 5 . a d d L a y o u t ( s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ t w ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ t w ) 
 
                 s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ l w   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ l w . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ w a l l _ s y s t e m _ l w " ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ l w ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ l w   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ l w . s e t O b j e c t N a m e ( " w g t _ f r a m e _ w a l l _ s y s t e m _ l w " ) 
 
                 s e l f . g r i d L a y o u t _ 2 6   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ l w ) 
 
                 s e l f . g r i d L a y o u t _ 2 6 . s e t C o n t e n t s M a r g i n s ( 0 ,   0 ,   0 ,   0 ) 
 
                 s e l f . g r i d L a y o u t _ 2 6 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 6 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ l w   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ l w . s e t O b j e c t N a m e ( " l a y _ f r a m e _ w a l l _ s y s t e m _ l w " ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 2   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ l w ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 2 . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 2 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ l w . a d d W i d g e t ( s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 2 ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 1   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ l w ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 1 . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 1 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ l w . a d d W i d g e t ( s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ l w _ w a l l 1 ) 
 
                 s e l f . g r i d L a y o u t _ 2 6 . a d d L a y o u t ( s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ l w ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ l w ) 
 
                 s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ a f   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ a f . s e t O b j e c t N a m e ( " l b l _ _ f r a m e _ w a l l _ s y s t e m _ a f " ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ a f ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ a f   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ a f . s e t O b j e c t N a m e ( " w g t _ f r a m e _ w a l l _ s y s t e m _ a f " ) 
 
                 s e l f . g r i d L a y o u t _ 2 7   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ a f ) 
 
                 s e l f . g r i d L a y o u t _ 2 7 . s e t C o n t e n t s M a r g i n s ( 0 ,   0 ,   0 ,   0 ) 
 
                 s e l f . g r i d L a y o u t _ 2 7 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 7 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ a f   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ a f . s e t O b j e c t N a m e ( " l a y _ f r a m e _ w a l l _ s y s t e m _ a f " ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ a f _ w a l l 1   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ a f ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ a f _ w a l l 1 . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ a f _ w a l l 1 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ a f . a d d W i d g e t ( s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ a f _ w a l l 1 ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ _ a f _ w a l l 2   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ a f ) 
 
                 s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ _ a f _ w a l l 2 . s e t O b j e c t N a m e ( " s p x _ f r a m e _ w a l l _ s y s t e m _ _ a f _ w a l l 2 " ) 
 
                 s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ a f . a d d W i d g e t ( s e l f . s p x _ f r a m e _ w a l l _ s y s t e m _ _ a f _ w a l l 2 ) 
 
                 s e l f . g r i d L a y o u t _ 2 7 . a d d L a y o u t ( s e l f . l a y _ f r a m e _ w a l l _ s y s t e m _ a f ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ f r a m e _ w a l l _ s y s t e m . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w g t _ f r a m e _ w a l l _ s y s t e m _ a f ) 
 
                 s e l f . g r i d L a y o u t _ 2 3 . a d d L a y o u t ( s e l f . f r m _ f r a m e _ w a l l _ s y s t e m ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 3 . a d d W i d g e t ( s e l f . g b x _ f r a m e _ w a l l _ s y s t e m ) 
 
                 s e l f . g b x _ d e s i g n   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . g b x _ d e s i g n . s e t O b j e c t N a m e ( " g b x _ d e s i g n " ) 
 
                 s e l f . g r i d L a y o u t _ 2 8   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . g r i d L a y o u t _ 2 8 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 8 " ) 
 
                 s e l f . f r m _ d e s i g n   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ d e s i g n . s e t O b j e c t N a m e ( " f r m _ d e s i g n " ) 
 
                 s e l f . l b l _ d e s i g n _ c o d e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . l b l _ d e s i g n _ c o d e . s e t O b j e c t N a m e ( " l b l _ d e s i g n _ c o d e " ) 
 
                 s e l f . f r m _ d e s i g n . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ d e s i g n _ c o d e ) 
 
                 s e l f . c b x _ d e s i g n _ d e s i g n _ c o d e   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . c b x _ d e s i g n _ d e s i g n _ c o d e . s e t O b j e c t N a m e ( " c b x _ d e s i g n _ d e s i g n _ c o d e " ) 
 
                 s e l f . f r m _ d e s i g n . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . c b x _ d e s i g n _ d e s i g n _ c o d e ) 
 
                 s e l f . l b l _ d e s i g n _ f r a m e _ s e i s m i c   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . l b l _ d e s i g n _ f r a m e _ s e i s m i c . s e t O b j e c t N a m e ( " l b l _ d e s i g n _ f r a m e _ s e i s m i c " ) 
 
                 s e l f . f r m _ d e s i g n . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ d e s i g n _ f r a m e _ s e i s m i c ) 
 
                 s e l f . c b x _ d e s i g n _ f r a m e _ s e i s m i c   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . c b x _ d e s i g n _ f r a m e _ s e i s m i c . s e t O b j e c t N a m e ( " c b x _ d e s i g n _ f r a m e _ s e i s m i c " ) 
 
                 s e l f . f r m _ d e s i g n . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . c b x _ d e s i g n _ f r a m e _ s e i s m i c ) 
 
                 s e l f . l b l _ d e s i g n _ w a l l s _ s e i s m i c   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . l b l _ d e s i g n _ w a l l s _ s e i s m i c . s e t O b j e c t N a m e ( " l b l _ d e s i g n _ w a l l s _ s e i s m i c " ) 
 
                 s e l f . f r m _ d e s i g n . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ d e s i g n _ w a l l s _ s e i s m i c ) 
 
                 s e l f . w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g . s e t O b j e c t N a m e ( " w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g " ) 
 
                 s e l f . g r i d L a y o u t _ 2 9   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ) 
 
                 s e l f . g r i d L a y o u t _ 2 9 . s e t C o n t e n t s M a r g i n s ( 0 ,   0 ,   0 ,   0 ) 
 
                 s e l f . g r i d L a y o u t _ 2 9 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 2 9 " ) 
 
                 s e l f . l a y _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g . s e t O b j e c t N a m e ( " l a y _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g " ) 
 
                 s e l f . c b x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ) 
 
                 s e l f . c b x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g . s e t O b j e c t N a m e ( " c b x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g " ) 
 
                 s e l f . l a y _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g . a d d W i d g e t ( s e l f . c b x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ) 
 
                 s e l f . s p x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ) 
 
                 s e l f . s p x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g . s e t O b j e c t N a m e ( " s p x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g " ) 
 
                 s e l f . l a y _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g . a d d W i d g e t ( s e l f . s p x _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ) 
 
                 s e l f . g r i d L a y o u t _ 2 9 . a d d L a y o u t ( s e l f . l a y _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ d e s i g n . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w g t _ d e s i g n _ w a l l _ s e i s m i c _ d e t a i l i n g ) 
 
                 s e l f . g r i d L a y o u t _ 2 8 . a d d L a y o u t ( s e l f . f r m _ d e s i g n ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ f o r m _ d a t a _ r o w _ 3 . a d d W i d g e t ( s e l f . g b x _ d e s i g n ) 
 
                 s e l f . l a y _ f r a m e _ d a t a . a d d L a y o u t ( s e l f . l a y _ f o r m _ d a t a _ r o w _ 3 ) 
 
                 s e l f . g r i d L a y o u t _ 4 . a d d L a y o u t ( s e l f . l a y _ f r a m e _ d a t a ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . b t n _ d e s i g n   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . t a b _ f r a m e _ d a t a ) 
 
                 s e l f . b t n _ d e s i g n . s e t O b j e c t N a m e ( " b t n _ d e s i g n " ) 
 
                 s e l f . g r i d L a y o u t _ 4 . a d d W i d g e t ( s e l f . b t n _ d e s i g n ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ f r a m e _ d a t a ,   " " ) 
 
                 s e l f . t a b _ d e s i g n _ r e s u l t s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ d e s i g n _ r e s u l t s . s e t O b j e c t N a m e ( " t a b _ d e s i g n _ r e s u l t s " ) 
 
                 s e l f . g r i d L a y o u t _ 3   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . g r i d L a y o u t _ 3 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 " ) 
 
                 s e l f . m p l _ d e s i g n _ r e s u l t s   =   M p l W i d g e t ( s e l f . t a b _ d e s i g n _ r e s u l t s ) 
 
                 s i z e P o l i c y   =   Q t W i d g e t s . Q S i z e P o l i c y ( Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m E x p a n d i n g ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m E x p a n d i n g ) 
 
                 s i z e P o l i c y . s e t H o r i z o n t a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t V e r t i c a l S t r e t c h ( 0 ) 
 
                 s i z e P o l i c y . s e t H e i g h t F o r W i d t h ( s e l f . m p l _ d e s i g n _ r e s u l t s . s i z e P o l i c y ( ) . h a s H e i g h t F o r W i d t h ( ) ) 
 
                 s e l f . m p l _ d e s i g n _ r e s u l t s . s e t S i z e P o l i c y ( s i z e P o l i c y ) 
 
                 s e l f . m p l _ d e s i g n _ r e s u l t s . s e t O b j e c t N a m e ( " m p l _ d e s i g n _ r e s u l t s " ) 
 
                 s e l f . g r i d L a y o u t _ 3 . a d d W i d g e t ( s e l f . m p l _ d e s i g n _ r e s u l t s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . v e r t i c a l L a y o u t   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . v e r t i c a l L a y o u t . s e t O b j e c t N a m e ( " v e r t i c a l L a y o u t " ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s   =   Q t W i d g e t s . Q T a b l e W i d g e t ( s e l f . t a b _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t O b j e c t N a m e ( " t b l _ d a t a _ d e s i g n _ c o l u m n s " ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t C o l u m n C o u n t ( 1 2 ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t R o w C o u n t ( 0 ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 0 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 1 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 2 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 3 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 4 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 5 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 6 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 7 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 8 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 9 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 1 0 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . s e t H o r i z o n t a l H e a d e r I t e m ( 1 1 ,   i t e m ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r ( ) . s e t D e f a u l t S e c t i o n S i z e ( 7 0 ) 
 
                 s e l f . v e r t i c a l L a y o u t . a d d W i d g e t ( s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s   =   Q t W i d g e t s . Q T a b l e W i d g e t ( s e l f . t a b _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t S t y l e S h e e t ( " f o n t :   8 p t   \ " M S   S h e l l   D l g   2 \ " ; " ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t O b j e c t N a m e ( " t b l _ d a t a _ d e s i g n _ b e a m s " ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t C o l u m n C o u n t ( 1 1 ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t R o w C o u n t ( 0 ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 0 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 f o n t   =   Q t G u i . Q F o n t ( ) 
 
                 f o n t . s e t B o l d ( F a l s e ) 
 
                 f o n t . s e t W e i g h t ( 5 0 ) 
 
                 i t e m . s e t F o n t ( f o n t ) 
 
                 i t e m . s e t B a c k g r o u n d ( Q t G u i . Q C o l o r ( 0 ,   0 ,   0 ) ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 1 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 2 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 3 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 4 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 5 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 6 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 7 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 8 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 9 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . s e t H o r i z o n t a l H e a d e r I t e m ( 1 0 ,   i t e m ) 
 
                 s e l f . v e r t i c a l L a y o u t . a d d W i d g e t ( s e l f . t b l _ d a t a _ d e s i g n _ b e a m s ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s   =   Q t W i d g e t s . Q T a b l e W i d g e t ( s e l f . t a b _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t O b j e c t N a m e ( " t b l _ d a t a _ d e s i g n _ w a l l s " ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t C o l u m n C o u n t ( 1 0 ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t R o w C o u n t ( 0 ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 0 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 1 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 2 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 3 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 4 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 5 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 6 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 7 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 f o n t   =   Q t G u i . Q F o n t ( ) 
 
                 f o n t . s e t P o i n t S i z e ( 9 ) 
 
                 i t e m . s e t F o n t ( f o n t ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 8 ,   i t e m ) 
 
                 i t e m   =   Q t W i d g e t s . Q T a b l e W i d g e t I t e m ( ) 
 
                 s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . s e t H o r i z o n t a l H e a d e r I t e m ( 9 ,   i t e m ) 
 
                 s e l f . v e r t i c a l L a y o u t . a d d W i d g e t ( s e l f . t b l _ d a t a _ d e s i g n _ w a l l s ) 
 
                 s e l f . b t n _ a c c e p t _ d e s i g n   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . t a b _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . b t n _ a c c e p t _ d e s i g n . s e t O b j e c t N a m e ( " b t n _ a c c e p t _ d e s i g n " ) 
 
                 s e l f . v e r t i c a l L a y o u t . a d d W i d g e t ( s e l f . b t n _ a c c e p t _ d e s i g n ) 
 
                 s e l f . g r i d L a y o u t _ 3 . a d d L a y o u t ( s e l f . v e r t i c a l L a y o u t ,   0 ,   2 ,   3 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ d e s i g n _ r e s u l t s ,   " " ) 
 
                 s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s . s e t O b j e c t N a m e ( " t a b _ n o n l i n e a r _ p a r a m e t e r s " ) 
 
                 s e l f . g r i d L a y o u t _ 1 6   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g r i d L a y o u t _ 1 6 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 6 " ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ p a r a m e t e r s " ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 " ) 
 
                 s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t O b j e c t N a m e ( " g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e " ) 
 
                 s e l f . g r i d L a y o u t _ 1 9   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . g r i d L a y o u t _ 1 9 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 1 9 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t O b j e c t N a m e ( " f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e " ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 . s e t O b j e c t N a m e ( " r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 . s e t O b j e c t N a m e ( " r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 . s e t O b j e c t N a m e ( " r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 . s e t O b j e c t N a m e ( " l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 " ) 
 
                 s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 ) 
 
                 s e l f . g r i d L a y o u t _ 1 9 . a d d L a y o u t ( s e l f . f r m _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e ) 
 
                 s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c . s e t O b j e c t N a m e ( " g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c " ) 
 
                 s e l f . g r i d L a y o u t _ 3 0   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . g r i d L a y o u t _ 3 0 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 0 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t O b j e c t N a m e ( " f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h " ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 . s e t O b j e c t N a m e ( " r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 . s e t O b j e c t N a m e ( " l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 . s e t O b j e c t N a m e ( " r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 . s e t O b j e c t N a m e ( " l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 . s e t O b j e c t N a m e ( " r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 . s e t O b j e c t N a m e ( " l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 . s e t T e x t ( " " ) 
 
                 s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 . s e t O b j e c t N a m e ( " r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 . s e t O b j e c t N a m e ( " l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 " ) 
 
                 s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 ) 
 
                 s e l f . g r i d L a y o u t _ 3 0 . a d d L a y o u t ( s e l f . f r m _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c ) 
 
                 s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l . s e t O b j e c t N a m e ( " g b x _ r a y l e i g h _ d a m p i n g _ m o d e l " ) 
 
                 s e l f . g r i d L a y o u t _ 3 1   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . g r i d L a y o u t _ 3 1 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 1 " ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l . s e t O b j e c t N a m e ( " f r m _ r e y l e i g h _ d a m p i n g _ m o d e l " ) 
 
                 s e l f . f r m _ r a y l e i g h _ d a m p i n g _ m o d e l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ r a y l e i g h _ d a m p i n g _ m o d e l . s e t O b j e c t N a m e ( " f r m _ r a y l e i g h _ d a m p i n g _ m o d e l " ) 
 
                 s e l f . r b n _ a s c e _ 4 1 _ 1 7   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . r b n _ a s c e _ 4 1 _ 1 7 . s e t O b j e c t N a m e ( " r b n _ a s c e _ 4 1 _ 1 7 " ) 
 
                 s e l f . f r m _ r a y l e i g h _ d a m p i n g _ m o d e l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ a s c e _ 4 1 _ 1 7 ) 
 
                 s e l f . r b n _ b a s e d _ o n _ t 1 _ t 3   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . r b n _ b a s e d _ o n _ t 1 _ t 3 . s e t O b j e c t N a m e ( " r b n _ b a s e d _ o n _ t 1 _ t 3 " ) 
 
                 s e l f . f r m _ r a y l e i g h _ d a m p i n g _ m o d e l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ b a s e d _ o n _ t 1 _ t 3 ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l . s e t L a y o u t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . f r m _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . l b l _ t a r g e t _ d a m p i n g _ r a t i o   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . l b l _ t a r g e t _ d a m p i n g _ r a t i o . s e t O b j e c t N a m e ( " l b l _ t a r g e t _ d a m p i n g _ r a t i o " ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t a r g e t _ d a m p i n g _ r a t i o ) 
 
                 s e l f . s p x _ t a r g e t _ d a m p i n g _ r a t i o   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . s p x _ t a r g e t _ d a m p i n g _ r a t i o . s e t O b j e c t N a m e ( " s p x _ t a r g e t _ d a m p i n g _ r a t i o " ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t a r g e t _ d a m p i n g _ r a t i o ) 
 
                 s e l f . l b l _ s t i f f n e s s _ m a t r i x   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . l b l _ s t i f f n e s s _ m a t r i x . s e t O b j e c t N a m e ( " l b l _ s t i f f n e s s _ m a t r i x " ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ s t i f f n e s s _ m a t r i x ) 
 
                 s e l f . l a y _ s t i f f n e s s _ m a t r i x   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ s t i f f n e s s _ m a t r i x . s e t O b j e c t N a m e ( " l a y _ s t i f f n e s s _ m a t r i x " ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c u r r e n t   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c u r r e n t . s e t O b j e c t N a m e ( " r b n _ s t i f f n e s s _ m a t r i x _ c u r r e n t " ) 
 
                 s e l f . l a y _ s t i f f n e s s _ m a t r i x . a d d W i d g e t ( s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c u r r e n t ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ i n i t i a l   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ i n i t i a l . s e t O b j e c t N a m e ( " r b n _ s t i f f n e s s _ m a t r i x _ i n i t i a l " ) 
 
                 s e l f . l a y _ s t i f f n e s s _ m a t r i x . a d d W i d g e t ( s e l f . r b n _ s t i f f n e s s _ m a t r i x _ i n i t i a l ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c o m m i t t e d   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c o m m i t t e d . s e t O b j e c t N a m e ( " r b n _ s t i f f n e s s _ m a t r i x _ c o m m i t t e d " ) 
 
                 s e l f . l a y _ s t i f f n e s s _ m a t r i x . a d d W i d g e t ( s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c o m m i t t e d ) 
 
                 s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l . s e t L a y o u t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l a y _ s t i f f n e s s _ m a t r i x ) 
 
                 s e l f . g r i d L a y o u t _ 3 1 . a d d L a y o u t ( s e l f . f r m _ r e y l e i g h _ d a m p i n g _ m o d e l ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l ) 
 
                 s e l f . g b x _ j o i n t _ m o d e l   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ j o i n t _ m o d e l . s e t O b j e c t N a m e ( " g b x _ j o i n t _ m o d e l " ) 
 
                 s e l f . g r i d L a y o u t _ 3 2   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ j o i n t _ m o d e l ) 
 
                 s e l f . g r i d L a y o u t _ 3 2 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 2 " ) 
 
                 s e l f . f o r m L a y o u t   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f o r m L a y o u t . s e t O b j e c t N a m e ( " f o r m L a y o u t " ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 1   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ j o i n t _ m o d e l ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 1 . s e t O b j e c t N a m e ( " r b n _ j o i n t _ m o d e l _ 1 " ) 
 
                 s e l f . f o r m L a y o u t . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ j o i n t _ m o d e l _ 1 ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 2   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ j o i n t _ m o d e l ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 2 . s e t O b j e c t N a m e ( " r b n _ j o i n t _ m o d e l _ 2 " ) 
 
                 s e l f . f o r m L a y o u t . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ j o i n t _ m o d e l _ 2 ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 3   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ j o i n t _ m o d e l ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 3 . s e t O b j e c t N a m e ( " r b n _ j o i n t _ m o d e l _ 3 " ) 
 
                 s e l f . f o r m L a y o u t . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ j o i n t _ m o d e l _ 3 ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ l i n e a r   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ j o i n t _ m o d e l ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ l i n e a r . s e t O b j e c t N a m e ( " r b n _ j o i n t _ m o d e l _ l i n e a r " ) 
 
                 s e l f . f o r m L a y o u t . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ j o i n t _ m o d e l _ l i n e a r ) 
 
                 s e l f . g r i d L a y o u t _ 3 2 . a d d L a y o u t ( s e l f . f o r m L a y o u t ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ j o i n t _ m o d e l ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 " ) 
 
                 s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n . s e t O b j e c t N a m e ( " g b x _ m a t e r i a l _ r e g u l a r i z a t i o n " ) 
 
                 s e l f . g r i d L a y o u t _ 3 3   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n ) 
 
                 s e l f . g r i d L a y o u t _ 3 3 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 3 " ) 
 
                 s e l f . f r m _ m a t e r i a l _ r e g u r a l i z a t i o n   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ m a t e r i a l _ r e g u r a l i z a t i o n . s e t O b j e c t N a m e ( " f r m _ m a t e r i a l _ r e g u r a l i z a t i o n " ) 
 
                 s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ c o n c r e t e   =   Q t W i d g e t s . Q C h e c k B o x ( s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n ) 
 
                 s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ c o n c r e t e . s e t O b j e c t N a m e ( " c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ c o n c r e t e " ) 
 
                 s e l f . f r m _ m a t e r i a l _ r e g u r a l i z a t i o n . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ c o n c r e t e ) 
 
                 s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ s t e e l   =   Q t W i d g e t s . Q C h e c k B o x ( s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n ) 
 
                 s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ s t e e l . s e t O b j e c t N a m e ( " c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ s t e e l " ) 
 
                 s e l f . f r m _ m a t e r i a l _ r e g u r a l i z a t i o n . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ s t e e l ) 
 
                 s e l f . g r i d L a y o u t _ 3 3 . a d d L a y o u t ( s e l f . f r m _ m a t e r i a l _ r e g u r a l i z a t i o n ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 . a d d W i d g e t ( s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n ) 
 
                 s e l f . g b x _ s h e a r _ m o d e l _ w a l l   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ s h e a r _ m o d e l _ w a l l . s e t O b j e c t N a m e ( " g b x _ s h e a r _ m o d e l _ w a l l " ) 
 
                 s e l f . g r i d L a y o u t _ 3 4   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ s h e a r _ m o d e l _ w a l l ) 
 
                 s e l f . g r i d L a y o u t _ 3 4 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 4 " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ w a l l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ w a l l . s e t O b j e c t N a m e ( " f r m _ s h e a r _ m o d e l _ w a l l " ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ l i n e a r   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s h e a r _ m o d e l _ w a l l ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ l i n e a r . s e t O b j e c t N a m e ( " r b n _ s h e a r _ m o d e l _ w a l l _ l i n e a r " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ w a l l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ l i n e a r ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ n o n l i n e a r   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s h e a r _ m o d e l _ w a l l ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ n o n l i n e a r . s e t O b j e c t N a m e ( " r b n _ s h e a r _ m o d e l _ w a l l _ n o n l i n e a r " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ w a l l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ n o n l i n e a r ) 
 
                 s e l f . g r i d L a y o u t _ 3 4 . a d d L a y o u t ( s e l f . f r m _ s h e a r _ m o d e l _ w a l l ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 . a d d W i d g e t ( s e l f . g b x _ s h e a r _ m o d e l _ w a l l ) 
 
                 s e l f . g b x _ s t e e l _ m o d e l   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ s t e e l _ m o d e l . s e t O b j e c t N a m e ( " g b x _ s t e e l _ m o d e l " ) 
 
                 s e l f . g r i d L a y o u t _ 3 5   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ s t e e l _ m o d e l ) 
 
                 s e l f . g r i d L a y o u t _ 3 5 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 5 " ) 
 
                 s e l f . f r m _ s t e e l _ m o d e l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ s t e e l _ m o d e l . s e t O b j e c t N a m e ( " f r m _ s t e e l _ m o d e l " ) 
 
                 s e l f . r b n _ s t e e l _ m o d e l _ h y s t e r e t i c   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s t e e l _ m o d e l ) 
 
                 s e l f . r b n _ s t e e l _ m o d e l _ h y s t e r e t i c . s e t O b j e c t N a m e ( " r b n _ s t e e l _ m o d e l _ h y s t e r e t i c " ) 
 
                 s e l f . f r m _ s t e e l _ m o d e l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s t e e l _ m o d e l _ h y s t e r e t i c ) 
 
                 s e l f . r b n _ s t e e l _ m o d e l _ s t e e l _ m p f   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s t e e l _ m o d e l ) 
 
                 s e l f . r b n _ s t e e l _ m o d e l _ s t e e l _ m p f . s e t O b j e c t N a m e ( " r b n _ s t e e l _ m o d e l _ s t e e l _ m p f " ) 
 
                 s e l f . f r m _ s t e e l _ m o d e l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s t e e l _ m o d e l _ s t e e l _ m p f ) 
 
                 s e l f . g r i d L a y o u t _ 3 5 . a d d L a y o u t ( s e l f . f r m _ s t e e l _ m o d e l ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 . a d d W i d g e t ( s e l f . g b x _ s t e e l _ m o d e l ) 
 
                 s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l . s e t O b j e c t N a m e ( " g b x _ e l e m e n t _ m o d e l _ w a l l " ) 
 
                 s e l f . g r i d L a y o u t _ 3 6   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l ) 
 
                 s e l f . g r i d L a y o u t _ 3 6 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 6 " ) 
 
                 s e l f . f r m _ e l e m e n t _ m o d e l _ w a l l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ e l e m e n t _ m o d e l _ w a l l . s e t O b j e c t N a m e ( " f r m _ e l e m e n t _ m o d e l _ w a l l " ) 
 
                 s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ f o r c e _ b e a m _ c o l u m n   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l ) 
 
                 s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ f o r c e _ b e a m _ c o l u m n . s e t O b j e c t N a m e ( " r b n _ e l e m e n t _ m o d e l _ w a l l _ f o r c e _ b e a m _ c o l u m n " ) 
 
                 s e l f . f r m _ e l e m e n t _ m o d e l _ w a l l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ f o r c e _ b e a m _ c o l u m n ) 
 
                 s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ n v l e m   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l ) 
 
                 s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ n v l e m . s e t O b j e c t N a m e ( " r b n _ e l e m e n t _ m o d e l _ w a l l _ n v l e m " ) 
 
                 s e l f . f r m _ e l e m e n t _ m o d e l _ w a l l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ n v l e m ) 
 
                 s e l f . g r i d L a y o u t _ 3 6 . a d d L a y o u t ( s e l f . f r m _ e l e m e n t _ m o d e l _ w a l l ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 . a d d W i d g e t ( s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 2 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 " ) 
 
                 s e l f . g b x _ s h e a r _ m o d e l _ f r a m e   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ s h e a r _ m o d e l _ f r a m e . s e t O b j e c t N a m e ( " g b x _ s h e a r _ m o d e l _ f r a m e " ) 
 
                 s e l f . g r i d L a y o u t _ 3 7   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ s h e a r _ m o d e l _ f r a m e ) 
 
                 s e l f . g r i d L a y o u t _ 3 7 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 7 " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ f r a m e   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ f r a m e . s e t O b j e c t N a m e ( " f r m _ s h e a r _ m o d e l _ f r a m e " ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n e   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s h e a r _ m o d e l _ f r a m e ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n e . s e t O b j e c t N a m e ( " r b n _ s h e a r _ m o d e l _ f r a m e _ n o n e " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ f r a m e . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n e ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ l i n e a r   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s h e a r _ m o d e l _ f r a m e ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ l i n e a r . s e t O b j e c t N a m e ( " r b n _ s h e a r _ m o d e l _ f r a m e _ l i n e a r " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ f r a m e . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ l i n e a r ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n l i n e a r   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ s h e a r _ m o d e l _ f r a m e ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n l i n e a r . s e t O b j e c t N a m e ( " r b n _ s h e a r _ m o d e l _ f r a m e _ n o n l i n e a r " ) 
 
                 s e l f . f r m _ s h e a r _ m o d e l _ f r a m e . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n l i n e a r ) 
 
                 s e l f . g r i d L a y o u t _ 3 7 . a d d L a y o u t ( s e l f . f r m _ s h e a r _ m o d e l _ f r a m e ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 . a d d W i d g e t ( s e l f . g b x _ s h e a r _ m o d e l _ f r a m e ) 
 
                 s e l f . g b x _ i n f i l l _ m o d e l _ w a l l   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ i n f i l l _ m o d e l _ w a l l . s e t O b j e c t N a m e ( " g b x _ i n f i l l _ m o d e l _ w a l l " ) 
 
                 s e l f . g r i d L a y o u t _ 3 8   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . g r i d L a y o u t _ 3 8 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 8 " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t O b j e c t N a m e ( " f r m _ i n f i l l _ m o d e l _ w a l l " ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ b e a m s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ b e a m s . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ w a l l _ b e a m s " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ b e a m s ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ b e a m s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ b e a m s . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ w a l l _ b e a m s " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ b e a m s ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ w a l l s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ w a l l s . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ w a l l _ w a l l s " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ w a l l s ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ w a l l s   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ w a l l s . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ w a l l _ w a l l s " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ w a l l _ w a l l s ) 
 
                 s e l f . g r i d L a y o u t _ 3 8 . a d d L a y o u t ( s e l f . f r m _ i n f i l l _ m o d e l _ w a l l ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 . a d d W i d g e t ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l ) 
 
                 s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t O b j e c t N a m e ( " g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 " ) 
 
                 s e l f . g r i d L a y o u t _ 3 9   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . g r i d L a y o u t _ 3 9 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 3 9 " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t O b j e c t N a m e ( " f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 " ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ t w   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ t w . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ t w " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ t w ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ t w   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ t w . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ t w " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ t w ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e ) 
 
                 s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t O b j e c t N a m e ( " w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 0   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . g r i d L a y o u t _ 4 0 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 0 " ) 
 
                 s e l f . l b l _ s p a c e _ 1   =   Q t W i d g e t s . Q L a b e l ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . l b l _ s p a c e _ 1 . s e t T e x t ( " " ) 
 
                 s e l f . l b l _ s p a c e _ 1 . s e t O b j e c t N a m e ( " l b l _ s p a c e _ 1 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 0 . a d d W i d g e t ( s e l f . l b l _ s p a c e _ 1 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t O b j e c t N a m e ( " f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 " ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m   =   Q t W i d g e t s . Q L a b e l ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m   =   Q t W i d g e t s . Q L a b e l ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c   =   Q t W i d g e t s . Q L a b e l ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c . s e t O b j e c t N a m e ( " l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c . s e t O b j e c t N a m e ( " s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c ) 
 
                 s e l f . g r i d L a y o u t _ 4 0 . a d d L a y o u t ( s e l f . f r m _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w d g _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . r b n _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . r b n _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t O b j e c t N a m e ( " r b n _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 ) 
 
                 s e l f . r b n _ s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ m a n u a l   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . r b n _ s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ m a n u a l . s e t O b j e c t N a m e ( " r b n _ s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ m a n u a l " ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ m a n u a l ) 
 
                 s e l f . w d g _ n o n l i n e a r _ m a n u a l   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . w d g _ n o n l i n e a r _ m a n u a l . s e t O b j e c t N a m e ( " w d g _ n o n l i n e a r _ m a n u a l " ) 
 
                 s e l f . g r i d L a y o u t _ 4 1   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . w d g _ n o n l i n e a r _ m a n u a l ) 
 
                 s e l f . g r i d L a y o u t _ 4 1 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 1 " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ m a n u a l   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ n o n l i n e a r _ m a n u a l . s e t O b j e c t N a m e ( " f r m _ n o n l i n e a r _ m a n u a l " ) 
 
                 s e l f . l b l _ n o n l i n e a r _ m a n u a l _ f m   =   Q t W i d g e t s . Q L a b e l ( s e l f . w d g _ n o n l i n e a r _ m a n u a l ) 
 
                 s e l f . l b l _ n o n l i n e a r _ m a n u a l _ f m . s e t O b j e c t N a m e ( " l b l _ n o n l i n e a r _ m a n u a l _ f m " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ m a n u a l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ n o n l i n e a r _ m a n u a l _ f m ) 
 
                 s e l f . s p x _ n o n l i n e a r _ m a n u a l _ f m   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . w d g _ n o n l i n e a r _ m a n u a l ) 
 
                 s e l f . s p x _ n o n l i n e a r _ m a n u a l _ f m . s e t O b j e c t N a m e ( " s p x _ n o n l i n e a r _ m a n u a l _ f m " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ m a n u a l . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ n o n l i n e a r _ m a n u a l _ f m ) 
 
                 s e l f . g r i d L a y o u t _ 4 1 . a d d L a y o u t ( s e l f . f r m _ n o n l i n e a r _ m a n u a l ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l b l _ s p a c e _ 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . w d g _ n o n l i n e a r _ m a n u a l ) 
 
                 s e l f . l b l _ s p a c e _ 2 . s e t T e x t ( " " ) 
 
                 s e l f . l b l _ s p a c e _ 2 . s e t O b j e c t N a m e ( " l b l _ s p a c e _ 2 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 1 . a d d W i d g e t ( s e l f . l b l _ s p a c e _ 2 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . w d g _ n o n l i n e a r _ m a n u a l ) 
 
                 s e l f . g r i d L a y o u t _ 3 9 . a d d L a y o u t ( s e l f . f r m _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 . a d d W i d g e t ( s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 ) 
 
                 s e l f . g b x _ o p e r a t i o n s   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . g b x _ o p e r a t i o n s . s e t O b j e c t N a m e ( " g b x _ o p e r a t i o n s " ) 
 
                 s e l f . g r i d L a y o u t _ 4 2   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ o p e r a t i o n s ) 
 
                 s e l f . g r i d L a y o u t _ 4 2 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 2 " ) 
 
                 s e l f . f o r m L a y o u t _ 3   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f o r m L a y o u t _ 3 . s e t O b j e c t N a m e ( " f o r m L a y o u t _ 3 " ) 
 
                 s e l f . l b l _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ o p e r a t i o n s ) 
 
                 s e l f . l b l _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s . s e t O b j e c t N a m e ( " l b l _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s " ) 
 
                 s e l f . f o r m L a y o u t _ 3 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s ) 
 
                 s e l f . s p x _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ o p e r a t i o n s ) 
 
                 s e l f . s p x _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s . s e t O b j e c t N a m e ( " s p x _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s " ) 
 
                 s e l f . f o r m L a y o u t _ 3 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s ) 
 
                 s e l f . g r i d L a y o u t _ 4 2 . a d d L a y o u t ( s e l f . f o r m L a y o u t _ 3 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 . a d d W i d g e t ( s e l f . g b x _ o p e r a t i o n s ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 3 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 4   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 4 . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 4 " ) 
 
                 s e l f . b t n _ c r e a t e _ n o n l i n e a r _ m o d e l   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) 
 
                 s e l f . b t n _ c r e a t e _ n o n l i n e a r _ m o d e l . s e t O b j e c t N a m e ( " b t n _ c r e a t e _ n o n l i n e a r _ m o d e l " ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 4 . a d d W i d g e t ( s e l f . b t n _ c r e a t e _ n o n l i n e a r _ m o d e l ) 
 
                 s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s _ r o w 4 ) 
 
                 s e l f . g r i d L a y o u t _ 1 6 . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ p a r a m e t e r s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ,   " " ) 
 
                 s e l f . t a b _ n o n l i n e a r _ a n a l y s i s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ n o n l i n e a r _ a n a l y s i s . s e t O b j e c t N a m e ( " t a b _ n o n l i n e a r _ a n a l y s i s " ) 
 
                 s e l f . g r i d L a y o u t _ 4 3   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ) 
 
                 s e l f . g r i d L a y o u t _ 4 3 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 3 " ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ a n a l y s i s " ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 " ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r . s e t O b j e c t N a m e ( " g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r " ) 
 
                 s e l f . g r i d L a y o u t _ 4 4   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r ) 
 
                 s e l f . g r i d L a y o u t _ 4 4 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 4 " ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r . s e t O b j e c t N a m e ( " l a y _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r " ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t O b j e c t N a m e ( " g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 5   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . g r i d L a y o u t _ 4 5 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 5 " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t O b j e c t N a m e ( " f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 " ) 
 
                 s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t r i a n g u l a r   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t r i a n g u l a r . s e t O b j e c t N a m e ( " l b l _ n o n l i n e a r _ a n a l y s i s _ t r i a n g u l a r " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t r i a n g u l a r ) 
 
                 s e l f . w g d _ l o a d _ p a t t e r n   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . w g d _ l o a d _ p a t t e r n . s e t O b j e c t N a m e ( " w g d _ l o a d _ p a t t e r n " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t   =   Q t W i d g e t s . Q H B o x L a y o u t ( s e l f . w g d _ l o a d _ p a t t e r n ) 
 
                 s e l f . h o r i z o n t a l L a y o u t . s e t O b j e c t N a m e ( " h o r i z o n t a l L a y o u t " ) 
 
                 s e l f . r b n _ l o a d _ p a t t e r n _ t r i a n g u l a r   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . w g d _ l o a d _ p a t t e r n ) 
 
                 s e l f . r b n _ l o a d _ p a t t e r n _ t r i a n g u l a r . s e t O b j e c t N a m e ( " r b n _ l o a d _ p a t t e r n _ t r i a n g u l a r " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t . a d d W i d g e t ( s e l f . r b n _ l o a d _ p a t t e r n _ t r i a n g u l a r ) 
 
                 s e l f . r b n _ l o a d _ p a t t e r n _ u n i f o r m   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . w g d _ l o a d _ p a t t e r n ) 
 
                 s e l f . r b n _ l o a d _ p a t t e r n _ u n i f o r m . s e t O b j e c t N a m e ( " r b n _ l o a d _ p a t t e r n _ u n i f o r m " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t . a d d W i d g e t ( s e l f . r b n _ l o a d _ p a t t e r n _ u n i f o r m ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . w g d _ l o a d _ p a t t e r n ) 
 
                 s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t y p e _ a n a l y s i s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t y p e _ a n a l y s i s . s e t O b j e c t N a m e ( " l b l _ n o n l i n e a r _ a n a l y s i s _ t y p e _ a n a l y s i s " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t y p e _ a n a l y s i s ) 
 
                 s e l f . w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s . s e t O b j e c t N a m e ( " w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 2   =   Q t W i d g e t s . Q H B o x L a y o u t ( s e l f . w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 2 . s e t O b j e c t N a m e ( " h o r i z o n t a l L a y o u t _ 2 " ) 
 
                 s e l f . r a d i o B u t t o n _ 3   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s ) 
 
                 s e l f . r a d i o B u t t o n _ 3 . s e t O b j e c t N a m e ( " r a d i o B u t t o n _ 3 " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 2 . a d d W i d g e t ( s e l f . r a d i o B u t t o n _ 3 ) 
 
                 s p a c e r I t e m   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 7 ,   2 0 ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 2 . a d d I t e m ( s p a c e r I t e m ) 
 
                 s e l f . r a d i o B u t t o n _ 4   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s ) 
 
                 s e l f . r a d i o B u t t o n _ 4 . s e t O b j e c t N a m e ( " r a d i o B u t t o n _ 4 " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 2 . a d d W i d g e t ( s e l f . r a d i o B u t t o n _ 4 ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . w g d _ l o a d _ p a t t e r n _ t y p e _ a n a l y s i s ) 
 
                 s e l f . l b l _ d r i f t _ p l o t   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . l b l _ d r i f t _ p l o t . s e t O b j e c t N a m e ( " l b l _ d r i f t _ p l o t " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 6 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ d r i f t _ p l o t ) 
 
                 s e l f . w g d _ d r i f t _ p l o t   =   Q t W i d g e t s . Q W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . w g d _ d r i f t _ p l o t . s e t O b j e c t N a m e ( " w g d _ d r i f t _ p l o t " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 3   =   Q t W i d g e t s . Q H B o x L a y o u t ( s e l f . w g d _ d r i f t _ p l o t ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 3 . s e t O b j e c t N a m e ( " h o r i z o n t a l L a y o u t _ 3 " ) 
 
                 s e l f . c h k _ d r i f t _ p l o t _ s d r   =   Q t W i d g e t s . Q C h e c k B o x ( s e l f . w g d _ d r i f t _ p l o t ) 
 
                 s e l f . c h k _ d r i f t _ p l o t _ s d r . s e t O b j e c t N a m e ( " c h k _ d r i f t _ p l o t _ s d r " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 3 . a d d W i d g e t ( s e l f . c h k _ d r i f t _ p l o t _ s d r ) 
 
                 s p a c e r I t e m 1   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 8 ,   2 0 ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 3 . a d d I t e m ( s p a c e r I t e m 1 ) 
 
                 s e l f . c h k _ d r i f t _ p l o t _ r d r   =   Q t W i d g e t s . Q C h e c k B o x ( s e l f . w g d _ d r i f t _ p l o t ) 
 
                 s e l f . c h k _ d r i f t _ p l o t _ r d r . s e t O b j e c t N a m e ( " c h k _ d r i f t _ p l o t _ r d r " ) 
 
                 s e l f . h o r i z o n t a l L a y o u t _ 3 . a d d W i d g e t ( s e l f . c h k _ d r i f t _ p l o t _ r d r ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 7 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . w g d _ d r i f t _ p l o t ) 
 
                 s e l f . l b l _ a l p h a _ c u r v e s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . l b l _ a l p h a _ c u r v e s . s e t O b j e c t N a m e ( " l b l _ a l p h a _ c u r v e s " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 8 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ a l p h a _ c u r v e s ) 
 
                 s e l f . t x t _ a l p h a _ c u r v e s   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . t x t _ a l p h a _ c u r v e s . s e t O b j e c t N a m e ( " t x t _ a l p h a _ c u r v e s " ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t W i d g e t ( 8 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ a l p h a _ c u r v e s ) 
 
                 s p a c e r I t e m 2   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 0 ,   1 2 ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ) 
 
                 s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t I t e m ( 9 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s p a c e r I t e m 2 ) 
 
                 s e l f . g r i d L a y o u t _ 4 5 . a d d L a y o u t ( s e l f . f r m _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r . a d d W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 . s e t O b j e c t N a m e ( " g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 6   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . g r i d L a y o u t _ 4 6 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 6 " ) 
 
                 s e l f . f o r m L a y o u t _ 2   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t O b j e c t N a m e ( " f o r m L a y o u t _ 2 " ) 
 
                 s e l f . l b l _ t a r g e t _ s t o r y _ d r i f t _ r a t i o   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . l b l _ t a r g e t _ s t o r y _ d r i f t _ r a t i o . s e t O b j e c t N a m e ( " l b l _ t a r g e t _ s t o r y _ d r i f t _ r a t i o " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t a r g e t _ s t o r y _ d r i f t _ r a t i o ) 
 
                 s e l f . s p x _ t a r g e t _ s t o r y _ d r i f t _ r a t i o   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . s p x _ t a r g e t _ s t o r y _ d r i f t _ r a t i o . s e t O b j e c t N a m e ( " s p x _ t a r g e t _ s t o r y _ d r i f t _ r a t i o " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ t a r g e t _ s t o r y _ d r i f t _ r a t i o ) 
 
                 s e l f . l b l _ n u m b e r _ s t e p s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . l b l _ n u m b e r _ s t e p s . s e t O b j e c t N a m e ( " l b l _ n u m b e r _ s t e p s " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ n u m b e r _ s t e p s ) 
 
                 s e l f . s p x _ n u m b e r _ s t e p s   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . s p x _ n u m b e r _ s t e p s . s e t O b j e c t N a m e ( " s p x _ n u m b e r _ s t e p s " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ n u m b e r _ s t e p s ) 
 
                 s e l f . l b l _ o u t p u t _ p u s h o v e r _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . l b l _ o u t p u t _ p u s h o v e r _ f i l e . s e t O b j e c t N a m e ( " l b l _ o u t p u t _ p u s h o v e r _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ o u t p u t _ p u s h o v e r _ f i l e ) 
 
                 s e l f . t x t _ o u t p u t _ p u s h o v e r _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . t x t _ o u t p u t _ p u s h o v e r _ f i l e . s e t O b j e c t N a m e ( " t x t _ o u t p u t _ p u s h o v e r _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ o u t p u t _ p u s h o v e r _ f i l e ) 
 
                 s p a c e r I t e m 3   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 0 ,   1 3 ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t I t e m ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s p a c e r I t e m 3 ) 
 
                 s e l f . l b l _ t y p e _ c h a r t   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . l b l _ t y p e _ c h a r t . s e t O b j e c t N a m e ( " l b l _ t y p e _ c h a r t " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ t y p e _ c h a r t ) 
 
                 s e l f . r b n _ p h p _ p l a s t i c _ r o t a t i o n   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . r b n _ p h p _ p l a s t i c _ r o t a t i o n . s e t O b j e c t N a m e ( " r b n _ p h p _ p l a s t i c _ r o t a t i o n " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ p h p _ p l a s t i c _ r o t a t i o n ) 
 
                 s e l f . r b n _ a c c e p t a n c e _ c r i t e r i a _ a s c e _ 1 7 4 1   =   Q t W i d g e t s . Q R a d i o B u t t o n ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . r b n _ a c c e p t a n c e _ c r i t e r i a _ a s c e _ 1 7 4 1 . s e t O b j e c t N a m e ( " r b n _ a c c e p t a n c e _ c r i t e r i a _ a s c e _ 1 7 4 1 " ) 
 
                 s e l f . f o r m L a y o u t _ 2 . s e t W i d g e t ( 6 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . r b n _ a c c e p t a n c e _ c r i t e r i a _ a s c e _ 1 7 4 1 ) 
 
                 s e l f . g r i d L a y o u t _ 4 6 . a d d L a y o u t ( s e l f . f o r m L a y o u t _ 2 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r . a d d W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 ) 
 
                 s e l f . g r i d L a y o u t _ 4 4 . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . b t n _ r u n _ p u s h o v e r   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r ) 
 
                 s e l f . b t n _ r u n _ p u s h o v e r . s e t O b j e c t N a m e ( " b t n _ r u n _ p u s h o v e r " ) 
 
                 s e l f . g r i d L a y o u t _ 4 4 . a d d W i d g e t ( s e l f . b t n _ r u n _ p u s h o v e r ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s . s e t O b j e c t N a m e ( " g b x _ n o n l i n e a r _ a n a l y s i s _ c s s " ) 
 
                 s e l f . g r i d L a y o u t _ 4 7   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . g r i d L a y o u t _ 4 7 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 7 " ) 
 
                 s e l f . f o r m L a y o u t _ 4   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t O b j e c t N a m e ( " f o r m L a y o u t _ 4 " ) 
 
                 s e l f . l b l _ g r o u n d _ m o t i o n s _ d i r e c t o r y   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . l b l _ g r o u n d _ m o t i o n s _ d i r e c t o r y . s e t O b j e c t N a m e ( " l b l _ g r o u n d _ m o t i o n s _ d i r e c t o r y " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ g r o u n d _ m o t i o n s _ d i r e c t o r y ) 
 
                 s e l f . t x t _ g r o u n d _ m o t i o n s _ d i r e c t o r y   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . t x t _ g r o u n d _ m o t i o n s _ d i r e c t o r y . s e t O b j e c t N a m e ( " t x t _ g r o u n d _ m o t i o n s _ d i r e c t o r y " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ g r o u n d _ m o t i o n s _ d i r e c t o r y ) 
 
                 s e l f . l b l _ o u t p u t _ c s s _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . l b l _ o u t p u t _ c s s _ f i l e . s e t O b j e c t N a m e ( " l b l _ o u t p u t _ c s s _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ o u t p u t _ c s s _ f i l e ) 
 
                 s e l f . t x t _ p u t p u t _ c s s _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . t x t _ p u t p u t _ c s s _ f i l e . s e t O b j e c t N a m e ( " t x t _ p u t p u t _ c s s _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ p u t p u t _ c s s _ f i l e ) 
 
                 s e l f . l b l _ i n t e n s i t y _ m e a s u r e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . l b l _ i n t e n s i t y _ m e a s u r e . s e t O b j e c t N a m e ( " l b l _ i n t e n s i t y _ m e a s u r e " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i n t e n s i t y _ m e a s u r e ) 
 
                 s e l f . c b x _ i n t e n s i t y _ m e a s u r e   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . c b x _ i n t e n s i t y _ m e a s u r e . s e t O b j e c t N a m e ( " c b x _ i n t e n s i t y _ m e a s u r e " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . c b x _ i n t e n s i t y _ m e a s u r e ) 
 
                 s e l f . l b l _ s a v e _ h i s t o r y _ r e s u l t s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . l b l _ s a v e _ h i s t o r y _ r e s u l t s . s e t O b j e c t N a m e ( " l b l _ s a v e _ h i s t o r y _ r e s u l t s " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ s a v e _ h i s t o r y _ r e s u l t s ) 
 
                 s e l f . c h k _ s a v e _ h i s t o r y _ r e s u l t s   =   Q t W i d g e t s . Q C h e c k B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . c h k _ s a v e _ h i s t o r y _ r e s u l t s . s e t T e x t ( " " ) 
 
                 s e l f . c h k _ s a v e _ h i s t o r y _ r e s u l t s . s e t O b j e c t N a m e ( " c h k _ s a v e _ h i s t o r y _ r e s u l t s " ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . c h k _ s a v e _ h i s t o r y _ r e s u l t s ) 
 
                 s p a c e r I t e m 4   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 0 ,   1 2 ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ) 
 
                 s e l f . f o r m L a y o u t _ 4 . s e t I t e m ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s p a c e r I t e m 4 ) 
 
                 s e l f . g r i d L a y o u t _ 4 7 . a d d L a y o u t ( s e l f . f o r m L a y o u t _ 4 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . b t n _ r u n _ c s s   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . b t n _ r u n _ c s s . s e t O b j e c t N a m e ( " b t n _ r u n _ c s s " ) 
 
                 s e l f . g r i d L a y o u t _ 4 7 . a d d W i d g e t ( s e l f . b t n _ r u n _ c s s ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a . s e t O b j e c t N a m e ( " g b x _ n o n l i n e a r _ a n a l y s i s _ i d a " ) 
 
                 s e l f . g r i d L a y o u t _ 4 8   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . g r i d L a y o u t _ 4 8 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 8 " ) 
 
                 s e l f . f o r m L a y o u t _ 5   =   Q t W i d g e t s . Q F o r m L a y o u t ( ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t O b j e c t N a m e ( " f o r m L a y o u t _ 5 " ) 
 
                 s e l f . l b l _ i d a _ f i r s t _ i n t e n s i t y   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ f i r s t _ i n t e n s i t y . s e t O b j e c t N a m e ( " l b l _ i d a _ f i r s t _ i n t e n s i t y " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ f i r s t _ i n t e n s i t y ) 
 
                 s e l f . s p x _ i d a _ f i r s t _ i n t e n s i t y   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . s p x _ i d a _ f i r s t _ i n t e n s i t y . s e t O b j e c t N a m e ( " s p x _ i d a _ f i r s t _ i n t e n s i t y " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 0 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i d a _ f i r s t _ i n t e n s i t y ) 
 
                 s e l f . l b l _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p . s e t O b j e c t N a m e ( " l b l _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p ) 
 
                 s e l f . s p x _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . s p x _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p . s e t O b j e c t N a m e ( " s p x _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 1 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p ) 
 
                 s e l f . l b l _ i d a _ d r i f t _ c a p a c i t y   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ d r i f t _ c a p a c i t y . s e t O b j e c t N a m e ( " l b l _ i d a _ d r i f t _ c a p a c i t y " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ d r i f t _ c a p a c i t y ) 
 
                 s e l f . s p x _ i d a _ d r i f t _ c a p a c i t y   =   Q t W i d g e t s . Q D o u b l e S p i n B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . s p x _ i d a _ d r i f t _ c a p a c i t y . s e t O b j e c t N a m e ( " s p x _ i d a _ d r i f t _ c a p a c i t y " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 2 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i d a _ d r i f t _ c a p a c i t y ) 
 
                 s e l f . l b l _ i d a _ m a x i m u m _ n u m b e r _ r u n s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ m a x i m u m _ n u m b e r _ r u n s . s e t O b j e c t N a m e ( " l b l _ i d a _ m a x i m u m _ n u m b e r _ r u n s " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ m a x i m u m _ n u m b e r _ r u n s ) 
 
                 s e l f . s p x _ i d a _ m a x i m u m _ n u m b e r _ r u n s   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . s p x _ i d a _ m a x i m u m _ n u m b e r _ r u n s . s e t O b j e c t N a m e ( " s p x _ i d a _ m a x i m u m _ n u m b e r _ r u n s " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 3 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . s p x _ i d a _ m a x i m u m _ n u m b e r _ r u n s ) 
 
                 s e l f . l b l _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e . s e t O b j e c t N a m e ( " l b l _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e ) 
 
                 s e l f . t x t _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . t x t _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e . s e t O b j e c t N a m e ( " t x t _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 4 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e ) 
 
                 s e l f . l b l _ i d a _ o u t p u t _ i d a _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ o u t p u t _ i d a _ f i l e . s e t O b j e c t N a m e ( " l b l _ i d a _ o u t p u t _ i d a _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ o u t p u t _ i d a _ f i l e ) 
 
                 s e l f . t x t _ i d a _ o u t p u t _ i d a _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . t x t _ i d a _ o u t p u t _ i d a _ f i l e . s e t O b j e c t N a m e ( " t x t _ i d a _ o u t p u t _ i d a _ f i l e " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 5 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ i d a _ o u t p u t _ i d a _ f i l e ) 
 
                 s e l f . l b l _ i d a _ i n t e n s i t y _ m e a s u r e   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . l b l _ i d a _ i n t e n s i t y _ m e a s u r e . s e t O b j e c t N a m e ( " l b l _ i d a _ i n t e n s i t y _ m e a s u r e " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 6 ,   Q t W i d g e t s . Q F o r m L a y o u t . L a b e l R o l e ,   s e l f . l b l _ i d a _ i n t e n s i t y _ m e a s u r e ) 
 
                 s e l f . t x t _ i d a _ i n t e n s i t y _ m e a s u r e   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . t x t _ i d a _ i n t e n s i t y _ m e a s u r e . s e t O b j e c t N a m e ( " t x t _ i d a _ i n t e n s i t y _ m e a s u r e " ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t W i d g e t ( 6 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s e l f . t x t _ i d a _ i n t e n s i t y _ m e a s u r e ) 
 
                 s p a c e r I t e m 5   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 0 ,   1 2 ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ) 
 
                 s e l f . f o r m L a y o u t _ 5 . s e t I t e m ( 7 ,   Q t W i d g e t s . Q F o r m L a y o u t . F i e l d R o l e ,   s p a c e r I t e m 5 ) 
 
                 s e l f . g r i d L a y o u t _ 4 8 . a d d L a y o u t ( s e l f . f o r m L a y o u t _ 5 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . b t n _ r u n _ i d a d   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . b t n _ r u n _ i d a d . s e t O b j e c t N a m e ( " b t n _ r u n _ i d a d " ) 
 
                 s e l f . g r i d L a y o u t _ 4 8 . a d d W i d g e t ( s e l f . b t n _ r u n _ i d a d ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s   =   Q t W i d g e t s . Q G r o u p B o x ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s . s e t O b j e c t N a m e ( " g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s " ) 
 
                 s e l f . g r i d L a y o u t _ 5 0   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . g r i d L a y o u t _ 5 0 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 5 0 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9   =   Q t W i d g e t s . Q G r i d L a y o u t ( ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 4 9 " ) 
 
                 s e l f . t x t _ t 1   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . t x t _ t 1 . s e t E n a b l e d ( F a l s e ) 
 
                 s e l f . t x t _ t 1 . s e t R e a d O n l y ( T r u e ) 
 
                 s e l f . t x t _ t 1 . s e t O b j e c t N a m e ( " t x t _ t 1 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . t x t _ t 1 ,   2 ,   1 ,   1 ,   1 ) 
 
                 s e l f . t x t _ t 2   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . t x t _ t 2 . s e t E n a b l e d ( F a l s e ) 
 
                 s e l f . t x t _ t 2 . s e t R e a d O n l y ( T r u e ) 
 
                 s e l f . t x t _ t 2 . s e t O b j e c t N a m e ( " t x t _ t 2 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . t x t _ t 2 ,   2 ,   3 ,   1 ,   1 ) 
 
                 s e l f . l b l _ t 1   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . l b l _ t 1 . s e t O b j e c t N a m e ( " l b l _ t 1 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . l b l _ t 1 ,   2 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l b l _ t 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . l b l _ t 2 . s e t O b j e c t N a m e ( " l b l _ t 2 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . l b l _ t 2 ,   2 ,   2 ,   1 ,   1 ) 
 
                 s e l f . l b l _ t 3   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . l b l _ t 3 . s e t O b j e c t N a m e ( " l b l _ t 3 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . l b l _ t 3 ,   2 ,   4 ,   1 ,   1 ) 
 
                 s e l f . t x t _ t 3   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . t x t _ t 3 . s e t E n a b l e d ( F a l s e ) 
 
                 s e l f . t x t _ t 3 . s e t R e a d O n l y ( T r u e ) 
 
                 s e l f . t x t _ t 3 . s e t O b j e c t N a m e ( " t x t _ t 3 " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . t x t _ t 3 ,   2 ,   5 ,   1 ,   1 ) 
 
                 s e l f . l i n _ p e r i o d s   =   Q t W i d g e t s . Q F r a m e ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . l i n _ p e r i o d s . s e t F r a m e S h a p e ( Q t W i d g e t s . Q F r a m e . H L i n e ) 
 
                 s e l f . l i n _ p e r i o d s . s e t F r a m e S h a d o w ( Q t W i d g e t s . Q F r a m e . S u n k e n ) 
 
                 s e l f . l i n _ p e r i o d s . s e t O b j e c t N a m e ( " l i n _ p e r i o d s " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . l i n _ p e r i o d s ,   1 ,   0 ,   1 ,   6 ) 
 
                 s e l f . l b l _ p e r i o d s _ a f t e r _ g r a v i t y _ l o a d s   =   Q t W i d g e t s . Q L a b e l ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . l b l _ p e r i o d s _ a f t e r _ g r a v i t y _ l o a d s . s e t A l i g n m e n t ( Q t C o r e . Q t . A l i g n C e n t e r ) 
 
                 s e l f . l b l _ p e r i o d s _ a f t e r _ g r a v i t y _ l o a d s . s e t O b j e c t N a m e ( " l b l _ p e r i o d s _ a f t e r _ g r a v i t y _ l o a d s " ) 
 
                 s e l f . g r i d L a y o u t _ 4 9 . a d d W i d g e t ( s e l f . l b l _ p e r i o d s _ a f t e r _ g r a v i t y _ l o a d s ,   0 ,   0 ,   1 ,   6 ) 
 
                 s e l f . g r i d L a y o u t _ 5 0 . a d d L a y o u t ( s e l f . g r i d L a y o u t _ 4 9 ,   0 ,   0 ,   1 ,   1 ) 
 
                 s p a c e r I t e m 6   =   Q t W i d g e t s . Q S p a c e r I t e m ( 2 0 ,   4 0 ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ) 
 
                 s e l f . g r i d L a y o u t _ 5 0 . a d d I t e m ( s p a c e r I t e m 6 ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 . a d d W i d g e t ( s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s ) 
 
                 s e l f . l a y _ n o n l i n e a r _ a n a l y s i s . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ a n a l y s i s _ r o w 1 ) 
 
                 s e l f . g r i d L a y o u t _ 4 3 . a d d L a y o u t ( s e l f . l a y _ n o n l i n e a r _ a n a l y s i s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ,   " " ) 
 
                 s e l f . t a b _ p u s h o v e r _ r e s u l t s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ p u s h o v e r _ r e s u l t s . s e t O b j e c t N a m e ( " t a b _ p u s h o v e r _ r e s u l t s " ) 
 
                 s e l f . g r i d L a y o u t _ 5 2   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ p u s h o v e r _ r e s u l t s ) 
 
                 s e l f . g r i d L a y o u t _ 5 2 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 5 2 " ) 
 
                 s e l f . l a y _ p u s h o v e r _ r e s u l t s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ p u s h o v e r _ r e s u l t s . s e t O b j e c t N a m e ( " l a y _ p u s h o v e r _ r e s u l t s " ) 
 
                 s e l f . p l t _ p h p   =   M p l W i d g e t ( s e l f . t a b _ p u s h o v e r _ r e s u l t s ) 
 
                 s e l f . p l t _ p h p . s e t O b j e c t N a m e ( " p l t _ p h p " ) 
 
                 s e l f . l a y _ p u s h o v e r _ r e s u l t s . a d d W i d g e t ( s e l f . p l t _ p h p ) 
 
                 s e l f . p l t _ a l p h a _ c u r v e   =   M p l W i d g e t ( s e l f . t a b _ p u s h o v e r _ r e s u l t s ) 
 
                 s e l f . p l t _ a l p h a _ c u r v e . s e t O b j e c t N a m e ( " p l t _ a l p h a _ c u r v e " ) 
 
                 s e l f . l a y _ p u s h o v e r _ r e s u l t s . a d d W i d g e t ( s e l f . p l t _ a l p h a _ c u r v e ) 
 
                 s e l f . p l t _ p u s h _ c u r v e   =   M p l W i d g e t ( s e l f . t a b _ p u s h o v e r _ r e s u l t s ) 
 
                 s e l f . p l t _ p u s h _ c u r v e . s e t O b j e c t N a m e ( " p l t _ p u s h _ c u r v e " ) 
 
                 s e l f . l a y _ p u s h o v e r _ r e s u l t s . a d d W i d g e t ( s e l f . p l t _ p u s h _ c u r v e ) 
 
                 s e l f . g r i d L a y o u t _ 5 2 . a d d L a y o u t ( s e l f . l a y _ p u s h o v e r _ r e s u l t s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ p u s h o v e r _ r e s u l t s ,   " " ) 
 
                 s e l f . t a b _ i d a _ r e s u l t s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ i d a _ r e s u l t s . s e t O b j e c t N a m e ( " t a b _ i d a _ r e s u l t s " ) 
 
                 s e l f . g r i d L a y o u t _ 5 3   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . g r i d L a y o u t _ 5 3 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 5 3 " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s . s e t O b j e c t N a m e ( " l a y _ i d a _ r e s u l t s " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ p l o t s   =   Q t W i d g e t s . Q G r i d L a y o u t ( ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ p l o t s . s e t O b j e c t N a m e ( " l a y _ i d a _ r e s u l t s _ p l o t s " ) 
 
                 s e l f . p l t _ s d r _ s a   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . p l t _ s d r _ s a . s e t O b j e c t N a m e ( " p l t _ s d r _ s a " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ s d r _ s a ,   0 ,   1 ,   1 ,   1 ) 
 
                 s e l f . p l t _ r d r _ s a   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . p l t _ r d r _ s a . s e t O b j e c t N a m e ( " p l t _ r d r _ s a " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ r d r _ s a ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . p l t _ v b _ w _ s a   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . p l t _ v b _ w _ s a . s e t O b j e c t N a m e ( " p l t _ v b _ w _ s a " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ v b _ w _ s a ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . p l t _ f r a g i l i t y _ c u r v e   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . p l t _ f r a g i l i t y _ c u r v e . s e t O b j e c t N a m e ( " p l t _ f r a g i l i t y _ c u r v e " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ f r a g i l i t y _ c u r v e ,   1 ,   1 ,   1 ,   1 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s . a d d L a y o u t ( s e l f . l a y _ i d a _ r e s u l t s _ p l o t s ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t O b j e c t N a m e ( " l a y _ i d a _ r e s u l t s _ c o n t r o l s " ) 
 
                 s e l f . l b l _ i n p u t _ i d a _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . l b l _ i n p u t _ i d a _ f i l e . s e t O b j e c t N a m e ( " l b l _ i n p u t _ i d a _ f i l e " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ i n p u t _ i d a _ f i l e ) 
 
                 s e l f . t x t _ i n p u t _ i d a _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . t x t _ i n p u t _ i d a _ f i l e . s e t O b j e c t N a m e ( " t x t _ i n p u t _ i d a _ f i l e " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . t x t _ i n p u t _ i d a _ f i l e ) 
 
                 s e l f . l b l _ s d r _ m a x _ c u r v e s   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . l b l _ s d r _ m a x _ c u r v e s . s e t O b j e c t N a m e ( " l b l _ s d r _ m a x _ c u r v e s " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ s d r _ m a x _ c u r v e s ) 
 
                 s e l f . t x t _ s d r _ m a x _ c u r v e s   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . t x t _ s d r _ m a x _ c u r v e s . s e t O b j e c t N a m e ( " t x t _ s d r _ m a x _ c u r v e s " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . t x t _ s d r _ m a x _ c u r v e s ) 
 
                 s e l f . b t n _ i d a _ r e s u l t s _ p l o t   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . t a b _ i d a _ r e s u l t s ) 
 
                 s e l f . b t n _ i d a _ r e s u l t s _ p l o t . s e t O b j e c t N a m e ( " b t n _ i d a _ r e s u l t s _ p l o t " ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . b t n _ i d a _ r e s u l t s _ p l o t ) 
 
                 s p a c e r I t e m 7   =   Q t W i d g e t s . Q S p a c e r I t e m ( 4 0 ,   2 0 ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . a d d I t e m ( s p a c e r I t e m 7 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 0 ,   1 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 1 ,   1 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 2 ,   1 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 3 ,   1 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 4 ,   3 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 5 ,   2 0 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s . a d d L a y o u t ( s e l f . l a y _ i d a _ r e s u l t s _ c o n t r o l s ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s . s e t S t r e t c h ( 0 ,   2 0 ) 
 
                 s e l f . l a y _ i d a _ r e s u l t s . s e t S t r e t c h ( 1 ,   1 ) 
 
                 s e l f . g r i d L a y o u t _ 5 3 . a d d L a y o u t ( s e l f . l a y _ i d a _ r e s u l t s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ i d a _ r e s u l t s ,   " " ) 
 
                 s e l f . t a b _ c s s _ r e s u l t s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ c s s _ r e s u l t s . s e t O b j e c t N a m e ( " t a b _ c s s _ r e s u l t s " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ g r i d   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ g r i d . s e t O b j e c t N a m e ( " l a y _ c s s _ r e s u l t s _ g r i d " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s . s e t O b j e c t N a m e ( " l a y _ c s s _ r e s u l t s " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ p l o t s   =   Q t W i d g e t s . Q G r i d L a y o u t ( ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ p l o t s . s e t O b j e c t N a m e ( " l a y _ c s s _ r e s u l t s _ p l o t s " ) 
 
                 s e l f . p l t _ m a x r a _ i m _ c s s   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . p l t _ m a x r a _ i m _ c s s . s e t O b j e c t N a m e ( " p l t _ m a x r a _ i m _ c s s " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ m a x r a _ i m _ c s s ,   0 ,   1 ,   1 ,   1 ) 
 
                 s e l f . p l t _ s d r _ i m _ c s s   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . p l t _ s d r _ i m _ c s s . s e t O b j e c t N a m e ( " p l t _ s d r _ i m _ c s s " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ s d r _ i m _ c s s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . p l t _ v u _ v n _ i m _ c s s   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . p l t _ v u _ v n _ i m _ c s s . s e t O b j e c t N a m e ( " p l t _ v u _ v n _ i m _ c s s " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ v u _ v n _ i m _ c s s ,   1 ,   0 ,   1 ,   1 ) 
 
                 s e l f . p l t _ f r a g i l i t y _ c u r v e _ c s s _ r e s u l t   =   Q t W i d g e t s . Q W i d g e t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . p l t _ f r a g i l i t y _ c u r v e _ c s s _ r e s u l t . s e t O b j e c t N a m e ( " p l t _ f r a g i l i t y _ c u r v e _ c s s _ r e s u l t " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ p l o t s . a d d W i d g e t ( s e l f . p l t _ f r a g i l i t y _ c u r v e _ c s s _ r e s u l t ,   1 ,   1 ,   1 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s . a d d L a y o u t ( s e l f . l a y _ c s s _ r e s u l t s _ p l o t s ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t O b j e c t N a m e ( " l a y _ c s s _ r e s u l t s _ c o n t r o l s " ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e . s e t O b j e c t N a m e ( " l b l _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e ) 
 
                 s e l f . t x t _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . t x t _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e . s e t O b j e c t N a m e ( " t x t _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . t x t _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ c h o o s e _ f a b i l i t y _ c u r v e   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ c h o o s e _ f a b i l i t y _ c u r v e . s e t O b j e c t N a m e ( " l b l _ c s s _ r e s u l t s _ c h o o s e _ f a b i l i t y _ c u r v e " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ c s s _ r e s u l t s _ c h o o s e _ f a b i l i t y _ c u r v e ) 
 
                 s e l f . c b x _ c s s _ r e s u l t s _ c h o o s e _ f r a g i l i t y _ c u r v e   =   Q t W i d g e t s . Q C o m b o B o x ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . c b x _ c s s _ r e s u l t s _ c h o o s e _ f r a g i l i t y _ c u r v e . s e t O b j e c t N a m e ( " c b x _ c s s _ r e s u l t s _ c h o o s e _ f r a g i l i t y _ c u r v e " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . c b x _ c s s _ r e s u l t s _ c h o o s e _ f r a g i l i t y _ c u r v e ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ l i m i t _ s t a g e   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ l i m i t _ s t a g e . s e t O b j e c t N a m e ( " l b l _ c s s _ r e s u l t s _ l i m i t _ s t a g e " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ c s s _ r e s u l t s _ l i m i t _ s t a g e ) 
 
                 s e l f . t x t _ c s s _ r e s u l t s _ l i m i t _ s t a g e   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . t x t _ c s s _ r e s u l t s _ l i m i t _ s t a g e . s e t O b j e c t N a m e ( " t x t _ c s s _ r e s u l t s _ l i m i t _ s t a g e " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . t x t _ c s s _ r e s u l t s _ l i m i t _ s t a g e ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t . s e t O b j e c t N a m e ( " l b l _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t ) 
 
                 s e l f . t x t _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . t x t _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t . s e t O b j e c t N a m e ( " t x t _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . t x t _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ t m i n   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ t m i n . s e t O b j e c t N a m e ( " l b l _ c s s _ r e s u l t s _ t m i n " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ c s s _ r e s u l t s _ t m i n ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ t d r   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ t d r . s e t O b j e c t N a m e ( " l b l _ c s s _ r e s u l t s _ t d r " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . l b l _ c s s _ r e s u l t s _ t d r ) 
 
                 s e l f . s p x _ c s s _ r e s u l t s _ s d r   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . s p x _ c s s _ r e s u l t s _ s d r . s e t O b j e c t N a m e ( " s p x _ c s s _ r e s u l t s _ s d r " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . s p x _ c s s _ r e s u l t s _ s d r ) 
 
                 s e l f . b t n _ c s s _ r e s u l t s _ p l o t   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . t a b _ c s s _ r e s u l t s ) 
 
                 s e l f . b t n _ c s s _ r e s u l t s _ p l o t . s e t O b j e c t N a m e ( " b t n _ c s s _ r e s u l t s _ p l o t " ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d W i d g e t ( s e l f . b t n _ c s s _ r e s u l t s _ p l o t ) 
 
                 s p a c e r I t e m 8   =   Q t W i d g e t s . Q S p a c e r I t e m ( 4 0 ,   2 0 ,   Q t W i d g e t s . Q S i z e P o l i c y . E x p a n d i n g ,   Q t W i d g e t s . Q S i z e P o l i c y . M i n i m u m ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . a d d I t e m ( s p a c e r I t e m 8 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 0 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 1 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 2 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 3 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 4 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 5 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 6 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 7 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 8 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 9 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 1 0 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 1 1 ,   4 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s . s e t S t r e t c h ( 1 2 ,   7 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s . a d d L a y o u t ( s e l f . l a y _ c s s _ r e s u l t s _ c o n t r o l s ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s . s e t S t r e t c h ( 0 ,   2 0 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s . s e t S t r e t c h ( 1 ,   1 ) 
 
                 s e l f . l a y _ c s s _ r e s u l t s _ g r i d . a d d L a y o u t ( s e l f . l a y _ c s s _ r e s u l t s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ c s s _ r e s u l t s ,   " " ) 
 
                 s e l f . t a b _ c s s _ g r a p h s   =   Q t W i d g e t s . Q W i d g e t ( ) 
 
                 s e l f . t a b _ c s s _ g r a p h s . s e t O b j e c t N a m e ( " t a b _ c s s _ g r a p h s " ) 
 
                 s e l f . g r i d L a y o u t _ 5 1   =   Q t W i d g e t s . Q G r i d L a y o u t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . g r i d L a y o u t _ 5 1 . s e t O b j e c t N a m e ( " g r i d L a y o u t _ 5 1 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s   =   Q t W i d g e t s . Q V B o x L a y o u t ( ) 
 
                 s e l f . l a y _ c s s _ g r a p h s . s e t O b j e c t N a m e ( " l a y _ c s s _ g r a p h s " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s . s e t O b j e c t N a m e ( " l a y _ c s s _ g r a p h s _ p l o t s " ) 
 
                 s e l f . m p _ h a z a r d _ c s s _ s d r _ m a x   =   M p l W i d g e t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . m p _ h a z a r d _ c s s _ s d r _ m a x . s e t O b j e c t N a m e ( " m p _ h a z a r d _ c s s _ s d r _ m a x " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s . a d d W i d g e t ( s e l f . m p _ h a z a r d _ c s s _ s d r _ m a x ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ a l p h a _ m a x   =   M p l W i d g e t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ a l p h a _ m a x . s e t O b j e c t N a m e ( " m p l _ h a z a r d _ c s s _ a l p h a _ m a x " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s . a d d W i d g e t ( s e l f . m p l _ h a z a r d _ c s s _ a l p h a _ m a x ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ a c c e l _ m a x   =   M p l W i d g e t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ a c c e l _ m a x . s e t O b j e c t N a m e ( " m p l _ h a z a r d _ c s s _ a c c e l _ m a x " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s . a d d W i d g e t ( s e l f . m p l _ h a z a r d _ c s s _ a c c e l _ m a x ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ r e s i d _ d e s p l   =   M p l W i d g e t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ r e s i d _ d e s p l . s e t O b j e c t N a m e ( " m p l _ h a z a r d _ c s s _ r e s i d _ d e s p l " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s . a d d W i d g e t ( s e l f . m p l _ h a z a r d _ c s s _ r e s i d _ d e s p l ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ v u _ v n c o l   =   M p l W i d g e t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . m p l _ h a z a r d _ c s s _ v u _ v n c o l . s e t O b j e c t N a m e ( " m p l _ h a z a r d _ c s s _ v u _ v n c o l " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ p l o t s . a d d W i d g e t ( s e l f . m p l _ h a z a r d _ c s s _ v u _ v n c o l ) 
 
                 s e l f . l a y _ c s s _ g r a p h s . a d d L a y o u t ( s e l f . l a y _ c s s _ g r a p h s _ p l o t s ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s   =   Q t W i d g e t s . Q H B o x L a y o u t ( ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . s e t O b j e c t N a m e ( " l a y _ c s s _ g r a p h s _ c o n t r o l s " ) 
 
                 s e l f . l a b e l   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . l a b e l . s e t O b j e c t N a m e ( " l a b e l " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . l a b e l ) 
 
                 s e l f . l i n e E d i t   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . l i n e E d i t . s e t O b j e c t N a m e ( " l i n e E d i t " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . l i n e E d i t ) 
 
                 s e l f . l a b e l _ 2   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . l a b e l _ 2 . s e t O b j e c t N a m e ( " l a b e l _ 2 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . l a b e l _ 2 ) 
 
                 s e l f . l i n e E d i t _ 2   =   Q t W i d g e t s . Q L i n e E d i t ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . l i n e E d i t _ 2 . s e t O b j e c t N a m e ( " l i n e E d i t _ 2 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . l i n e E d i t _ 2 ) 
 
                 s e l f . l a b e l _ 3   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . l a b e l _ 3 . s e t O b j e c t N a m e ( " l a b e l _ 3 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . l a b e l _ 3 ) 
 
                 s e l f . s p i n B o x _ 2   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . s p i n B o x _ 2 . s e t O b j e c t N a m e ( " s p i n B o x _ 2 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . s p i n B o x _ 2 ) 
 
                 s e l f . l a b e l _ 4   =   Q t W i d g e t s . Q L a b e l ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . l a b e l _ 4 . s e t O b j e c t N a m e ( " l a b e l _ 4 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . l a b e l _ 4 ) 
 
                 s e l f . s p i n B o x _ 3   =   Q t W i d g e t s . Q S p i n B o x ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . s p i n B o x _ 3 . s e t O b j e c t N a m e ( " s p i n B o x _ 3 " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . s p i n B o x _ 3 ) 
 
                 s e l f . b t n _ p l o t _ c s s _ m a x _ f l o o r s   =   Q t W i d g e t s . Q P u s h B u t t o n ( s e l f . t a b _ c s s _ g r a p h s ) 
 
                 s e l f . b t n _ p l o t _ c s s _ m a x _ f l o o r s . s e t O b j e c t N a m e ( " b t n _ p l o t _ c s s _ m a x _ f l o o r s " ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . a d d W i d g e t ( s e l f . b t n _ p l o t _ c s s _ m a x _ f l o o r s ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . s e t S t r e t c h ( 7 ,   2 ) 
 
                 s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s . s e t S t r e t c h ( 8 ,   6 ) 
 
                 s e l f . l a y _ c s s _ g r a p h s . a d d L a y o u t ( s e l f . l a y _ c s s _ g r a p h s _ c o n t r o l s ) 
 
                 s e l f . l a y _ c s s _ g r a p h s . s e t S t r e t c h ( 0 ,   2 0 ) 
 
                 s e l f . l a y _ c s s _ g r a p h s . s e t S t r e t c h ( 1 ,   1 ) 
 
                 s e l f . g r i d L a y o u t _ 5 1 . a d d L a y o u t ( s e l f . l a y _ c s s _ g r a p h s ,   0 ,   0 ,   1 ,   1 ) 
 
                 s e l f . t w d _ p r i n c i p a l . a d d T a b ( s e l f . t a b _ c s s _ g r a p h s ,   " " ) 
 
                 s e l f . l a y _ p r i n c i p a l . a d d W i d g e t ( s e l f . t w d _ p r i n c i p a l ) 
 
                 s e l f . l a y _ s e c c i o n e s . a d d L a y o u t ( s e l f . l a y _ p r i n c i p a l ) 
 
                 s e l f . l b l _ p i e _ p a g i n a   =   Q t W i d g e t s . Q L a b e l ( s e l f . c e n t r a l w i d g e t ) 
 
                 s e l f . l b l _ p i e _ p a g i n a . s e t T e x t ( " " ) 
 
                 s e l f . l b l _ p i e _ p a g i n a . s e t P i x m a p ( Q t G u i . Q P i x m a p ( " . \ \ b a n n e r _ a b a j o . j p g " ) ) 
 
                 s e l f . l b l _ p i e _ p a g i n a . s e t O b j e c t N a m e ( " l b l _ p i e _ p a g i n a " ) 
 
                 s e l f . l a y _ s e c c i o n e s . a d d W i d g e t ( s e l f . l b l _ p i e _ p a g i n a ) 
 
                 s e l f . l a y _ s e c c i o n e s . s e t S t r e t c h ( 0 ,   1 ) 
 
                 s e l f . l a y _ s e c c i o n e s . s e t S t r e t c h ( 1 ,   2 0 ) 
 
                 s e l f . l a y _ s e c c i o n e s . s e t S t r e t c h ( 2 ,   1 ) 
 
                 s e l f . g r i d L a y o u t . a d d L a y o u t ( s e l f . l a y _ s e c c i o n e s ,   0 ,   0 ,   1 ,   1 ) 
 
                 N o n L i n e a r M a i n W i n d o w . s e t C e n t r a l W i d g e t ( s e l f . c e n t r a l w i d g e t ) 
 
                 s e l f . m b r _ p r i n c i p a l   =   Q t W i d g e t s . Q M e n u B a r ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m b r _ p r i n c i p a l . s e t G e o m e t r y ( Q t C o r e . Q R e c t ( 0 ,   0 ,   2 5 5 1 ,   2 1 ) ) 
 
                 s e l f . m b r _ p r i n c i p a l . s e t O b j e c t N a m e ( " m b r _ p r i n c i p a l " ) 
 
                 s e l f . m n u _ f i l e   =   Q t W i d g e t s . Q M e n u ( s e l f . m b r _ p r i n c i p a l ) 
 
                 s e l f . m n u _ f i l e . s e t O b j e c t N a m e ( " m n u _ f i l e " ) 
 
                 s e l f . m n u _ a y u d a   =   Q t W i d g e t s . Q M e n u ( s e l f . m b r _ p r i n c i p a l ) 
 
                 s e l f . m n u _ a y u d a . s e t O b j e c t N a m e ( " m n u _ a y u d a " ) 
 
                 s e l f . m n u _ d e s i g n _ r e s u l t s   =   Q t W i d g e t s . Q M e n u ( s e l f . m b r _ p r i n c i p a l ) 
 
                 s e l f . m n u _ d e s i g n _ r e s u l t s . s e t O b j e c t N a m e ( " m n u _ d e s i g n _ r e s u l t s " ) 
 
                 s e l f . m n u _ b e a m _ d a t a   =   Q t W i d g e t s . Q M e n u ( s e l f . m n u _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . m n u _ b e a m _ d a t a . s e t O b j e c t N a m e ( " m n u _ b e a m _ d a t a " ) 
 
                 s e l f . m n u _ c o l u m n _ d a t a   =   Q t W i d g e t s . Q M e n u ( s e l f . m n u _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . m n u _ c o l u m n _ d a t a . s e t O b j e c t N a m e ( " m n u _ c o l u m n _ d a t a " ) 
 
                 s e l f . m n u _ w a l l _ d a t a   =   Q t W i d g e t s . Q M e n u ( s e l f . m n u _ d e s i g n _ r e s u l t s ) 
 
                 s e l f . m n u _ w a l l _ d a t a . s e t O b j e c t N a m e ( " m n u _ w a l l _ d a t a " ) 
 
                 N o n L i n e a r M a i n W i n d o w . s e t M e n u B a r ( s e l f . m b r _ p r i n c i p a l ) 
 
                 s e l f . s t a t u s b a r   =   Q t W i d g e t s . Q S t a t u s B a r ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . s t a t u s b a r . s e t O b j e c t N a m e ( " s t a t u s b a r " ) 
 
                 N o n L i n e a r M a i n W i n d o w . s e t S t a t u s B a r ( s e l f . s t a t u s b a r ) 
 
                 s e l f . m n i _ l o a d _ f i l e   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ l o a d _ f i l e . s e t O b j e c t N a m e ( " m n i _ l o a d _ f i l e " ) 
 
                 s e l f . m n i _ e x i t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ e x i t . s e t O b j e c t N a m e ( " m n i _ e x i t " ) 
 
                 s e l f . m n i _ a c e r c a _ d e   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ a c e r c a _ d e . s e t O b j e c t N a m e ( " m n i _ a c e r c a _ d e " ) 
 
                 s e l f . m n i _ b e a m _ d a t a _ i m p o r t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ b e a m _ d a t a _ i m p o r t . s e t O b j e c t N a m e ( " m n i _ b e a m _ d a t a _ i m p o r t " ) 
 
                 s e l f . m n i _ b e a m _ d a t a _ e x p o r t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ b e a m _ d a t a _ e x p o r t . s e t O b j e c t N a m e ( " m n i _ b e a m _ d a t a _ e x p o r t " ) 
 
                 s e l f . m n i _ c o l u m n _ d a t a _ e x p o r t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ c o l u m n _ d a t a _ e x p o r t . s e t O b j e c t N a m e ( " m n i _ c o l u m n _ d a t a _ e x p o r t " ) 
 
                 s e l f . m n i _ c o l u m n _ d a t a _ i m p o r t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ c o l u m n _ d a t a _ i m p o r t . s e t O b j e c t N a m e ( " m n i _ c o l u m n _ d a t a _ i m p o r t " ) 
 
                 s e l f . m n i _ w a l l _ d a t a _ i m p o r t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ w a l l _ d a t a _ i m p o r t . s e t O b j e c t N a m e ( " m n i _ w a l l _ d a t a _ i m p o r t " ) 
 
                 s e l f . m n i _ w a l l _ d a t a _ e x p o r t   =   Q t W i d g e t s . Q A c t i o n ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . m n i _ w a l l _ d a t a _ e x p o r t . s e t O b j e c t N a m e ( " m n i _ w a l l _ d a t a _ e x p o r t " ) 
 
                 s e l f . m n u _ f i l e . a d d A c t i o n ( s e l f . m n i _ l o a d _ f i l e ) 
 
                 s e l f . m n u _ f i l e . a d d S e p a r a t o r ( ) 
 
                 s e l f . m n u _ f i l e . a d d A c t i o n ( s e l f . m n i _ e x i t ) 
 
                 s e l f . m n u _ a y u d a . a d d A c t i o n ( s e l f . m n i _ a c e r c a _ d e ) 
 
                 s e l f . m n u _ b e a m _ d a t a . a d d A c t i o n ( s e l f . m n i _ b e a m _ d a t a _ i m p o r t ) 
 
                 s e l f . m n u _ b e a m _ d a t a . a d d A c t i o n ( s e l f . m n i _ b e a m _ d a t a _ e x p o r t ) 
 
                 s e l f . m n u _ c o l u m n _ d a t a . a d d A c t i o n ( s e l f . m n i _ c o l u m n _ d a t a _ i m p o r t ) 
 
                 s e l f . m n u _ c o l u m n _ d a t a . a d d A c t i o n ( s e l f . m n i _ c o l u m n _ d a t a _ e x p o r t ) 
 
                 s e l f . m n u _ w a l l _ d a t a . a d d A c t i o n ( s e l f . m n i _ w a l l _ d a t a _ i m p o r t ) 
 
                 s e l f . m n u _ w a l l _ d a t a . a d d A c t i o n ( s e l f . m n i _ w a l l _ d a t a _ e x p o r t ) 
 
                 s e l f . m n u _ d e s i g n _ r e s u l t s . a d d A c t i o n ( s e l f . m n u _ b e a m _ d a t a . m e n u A c t i o n ( ) ) 
 
                 s e l f . m n u _ d e s i g n _ r e s u l t s . a d d A c t i o n ( s e l f . m n u _ c o l u m n _ d a t a . m e n u A c t i o n ( ) ) 
 
                 s e l f . m n u _ d e s i g n _ r e s u l t s . a d d A c t i o n ( s e l f . m n u _ w a l l _ d a t a . m e n u A c t i o n ( ) ) 
 
                 s e l f . m b r _ p r i n c i p a l . a d d A c t i o n ( s e l f . m n u _ f i l e . m e n u A c t i o n ( ) ) 
 
                 s e l f . m b r _ p r i n c i p a l . a d d A c t i o n ( s e l f . m n u _ d e s i g n _ r e s u l t s . m e n u A c t i o n ( ) ) 
 
                 s e l f . m b r _ p r i n c i p a l . a d d A c t i o n ( s e l f . m n u _ a y u d a . m e n u A c t i o n ( ) ) 
 
 
 
                 s e l f . r e t r a n s l a t e U i ( N o n L i n e a r M a i n W i n d o w ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t C u r r e n t I n d e x ( 0 ) 
 
                 Q t C o r e . Q M e t a O b j e c t . c o n n e c t S l o t s B y N a m e ( N o n L i n e a r M a i n W i n d o w ) 
 
 
 
         d e f   r e t r a n s l a t e U i ( s e l f ,   N o n L i n e a r M a i n W i n d o w ) : 
 
                 _ t r a n s l a t e   =   Q t C o r e . Q C o r e A p p l i c a t i o n . t r a n s l a t e 
 
                 N o n L i n e a r M a i n W i n d o w . s e t W i n d o w T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R C - F I A P " ) ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ c o l u m n _ s e c t i o n s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o l u m n s   s e c t i o n s " ) ) 
 
                 s e l f . g b x _ c o l u m n s _ s e c t i o n s _ e x t e r i o r . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " E x t e r i o r " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ w i d t h . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W i d t h   ( m ) : " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ d e p t h . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e p t h   ( m ) " ) ) 
 
                 s e l f . g b x _ c o l u m n s _ s e c t i o n s _ i n t e r i o r . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n t e r i o r " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ w i d t h . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W i d t h   ( m ) : " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ s e c t i o n s _ i n t e r i o r _ d e p t h . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e p t h   ( m ) : " ) ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ b e a m s _ s e c t i o n s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " B e a m s   s e c t i o n s " ) ) 
 
                 s e l f . l b l _ b e a m _ s e c t i o n s _ w i d t h . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W i d t h   ( m ) : " ) ) 
 
                 s e l f . l b l _ b e a m _ s e c t i o n s _ d e p t h . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e p t h : " ) ) 
 
                 s e l f . g b x _ f o r m _ d a t a _ f i l a _ 1 _ s e i s m i c _ l o a d . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S e i s m i c   l o a d   c o d e   a n d   p e r f o r m a n c e " ) ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R : " ) ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ c d . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C d : " ) ) 
 
                 s e l f . l b l _ _ s e i s m i c _ l o a d _ o m e g a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " l%#: " ) ) 
 
                 s e l f . l b l _ s e i s m i c _ l o a d _ i . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I : " ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T y p e   l o a d " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S e i s m i c   t y p e   l o a d : " ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t I t e m T e x t ( 0 ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S p e c t r a   f i l e " ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t I t e m T e x t ( 1 ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A S C E   7 - 1 6 " ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t I t e m T e x t ( 2 ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N S R - 1 0 " ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t I t e m T e x t ( 3 ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N S R - 9 8 " ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t I t e m T e x t ( 4 ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C C C S R - 8 4 " ) ) 
 
                 s e l f . c b x _ t y p e _ l o a d _ s e i s m i c _ t y p e _ l o a d . s e t I t e m T e x t ( 5 ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W e i g h t   P e r c e n t a g e " ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S p e c t r a   f i l e   s e l e c t o r " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ s p e c t r a _ f i l e _ s e l e c t o r _ s p e c t _ t e x t _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S p e c t   t e x t   f i l e : " ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ a s c e _ 7 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A S C E   7 - 1 6   S e i s m i c   l o a d   p a r a m e t e r s " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > S < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > D S   < / s p a n > ( g ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ s d 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > S < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > D 1   < / s p a n > ( g ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ a s c e _ 7 _ t l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > T < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > L   < / s p a n > ( s e c ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 1 0 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   "   N S R - 1 0   S e i s m i c   l o a d   p a r a m e t e r s " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A a : " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 1 0 _ a v . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A v : " ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ n s r 9 8 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N S R - 9 8   S e i s m i c   l o a d   p a r a m e t e r s " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ a a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A a : " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ n s r 9 8 _ s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S : " ) ) 
 
                 s e l f . g b x _ t y p e _ l o a d _ c c c s r 8 4 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C C C S R - 8 4   S e i s m i c   l o a d   p a r a m e t e r s " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A a : " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ a v . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A v : " ) ) 
 
                 s e l f . l b l _ t y p e _ l o a d _ c c c s r 8 4 _ s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S : " ) ) 
 
                 s e l f . g b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S e i s m i c   l o a d   c o e f f i c i e n t ,   C S =   V b / W " ) ) 
 
                 s e l f . l b x _ s e i s m i c _ l o a d _ c o e f f i c i e n t _ p e r c e n t a g e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " % : " ) ) 
 
                 s e l f . g b x _ f r a m e _ g e o m e t r y . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F r a m e   g e o m e t r y " ) ) 
 
                 s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s t o r y . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " V e c t o r   o f   s t o r y   h e i g t h s   ( m ) : " ) ) 
 
                 s e l f . l b l _ f r a m e _ g e o m e t r y _ v e c t o r _ s p a n s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " V e c t o r   o f   s p a n s   ( m ) : " ) ) 
 
                 s e l f . g b x _ f r a m e _ t y p e . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F r a m e   t y p e : " ) ) 
 
                 s e l f . r b n _ f r a m e _ t y p e _ s p a t i a l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S p a t i a l " ) ) 
 
                 s e l f . r b n _ f r a m e _ t y p e _ p e r i m e t r a l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P e r i m e t r a l " ) ) 
 
                 s e l f . g b x _ f r a m e _ t r i b u t a r y . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F r a m e   t r i b u t a r y   g r a v i t y   l o a d i n g " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ d e a d _ l o a d . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e a d   l o a d   ( k N / M 2 ) " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ l i v e _ l o a d . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L i v e   l o a d   ( k N / M 2 ) " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ g r a v i t y . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T r i b u t a r y   l e n g t h   f o r   g r a v i t y " ) ) 
 
                 s e l f . l b l _ f r a m e _ t r i b u t a r y _ t r i b u t a r y _ l e n g t h _ s e i s m i c . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T r i b u t a r y   l e n g t h   f o r   s e i s m i c " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ p d e l t a _ l e a n i n g _ c o l u m n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P D e l t a   l e a n i n g   c o l u m n " ) ) 
 
                 s e l f . r b n _ f r a m e _ t r i b u t a r y _ y e s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " Y e s " ) ) 
 
                 s e l f . r b n _ f r a m e _ t r i b u t a r y _ n o . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ t r i b u t a r y _ i n e r t i a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n e r t i a " ) ) 
 
                 s e l f . g b x _ m e m b e r . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M e m b e r " ) ) 
 
                 s e l f . l b l _ m e m b e r _ m e m b e r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M e m b e r " ) ) 
 
                 s e l f . l b l _ m e m b e r _ m o m e n t _ f o r _ i n t e r t i a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M o m e n t   o f   i n e r t i a   f o r   e l a s t i c   a n a l y s i s " ) ) 
 
                 s e l f . l b l _ m e m b e r _ c o l u m n s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o l u m n s : " ) ) 
 
                 s e l f . l b l _ m e m b e r _ b e a m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " B e a m : " ) ) 
 
                 s e l f . l b l _ m e m b e r _ w a l l s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l s : " ) ) 
 
                 s e l f . g b x _ m a t e r i a l s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M a t e r i a l s " ) ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ l o n g . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > f < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > y < / s p a n >   l o n g .   ( M P a ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ t r a n s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > f < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > y < / s p a n >   t r a n s v .   ( M P a ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ m a t e r i a l s _ f _ b e a m s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > f ,%$%< s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > c < / s p a n >   b e a m s   ( M P a ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . s p x _ m a t e r i a l s _ f _ c o l u m n s _ 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > f ,%$%< s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > c < / s p a n >   c o l u m n s   ( M P a ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . g b x _ c o l u m n _ b e a m . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o l u m n - t o - b e a m " ) ) 
 
                 s e l f . l b l _ _ c o l u m n _ b e a m _ m i n i m u m _ c o l u m n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M i n i m u m   c o l u m n - t o - b e a m \ n " 
 
 " m o m e n t   s t r e n g t h   r a t i o : " ) ) 
 
                 s e l f . g b x _ f r a m e _ w a l l _ s y s t e m . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F r a m e - w a l l   s y s t e m   i n p u t   d a t a : " ) ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ n u m b e r _ f r a m e s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N u m b e r   o f   f r a m e s : " ) ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l   1 " ) ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ w a l l s _ w a l l 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l   2 " ) ) 
 
                 s e l f . l b l _ f r a m e _ w a l l _ s y s t e m _ t w . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " t w   ( m ) : " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ l w . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " l w   ( m ) : " ) ) 
 
                 s e l f . l b l _ _ f r a m e _ w a l l _ s y s t e m _ a f . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > A f   ( m < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u p e r ; \ " > 2 < / s p a n > ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . g b x _ d e s i g n . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e s i g n " ) ) 
 
                 s e l f . l b l _ d e s i g n _ c o d e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e s i g n   c o d e " ) ) 
 
                 s e l f . l b l _ d e s i g n _ f r a m e _ s e i s m i c . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F r a m e   s e i s m i c   d e t a i l i n g : " ) ) 
 
                 s e l f . l b l _ d e s i g n _ w a l l s _ s e i s m i c . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l   s e i s m i c   d e t a i l i n g : " ) ) 
 
                 s e l f . b t n _ d e s i g n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e s i g n " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ f r a m e _ d a t a ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F r a m e   D a t a " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 0 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I D " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 1 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " b \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 2 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " h \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 3 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " g%� " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 4 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " d b \ n " 
 
 " [ m m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 5 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " d s t \ n " 
 
 " [ m m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 6 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " n b H " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 7 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " n b B " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 8 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L e g   #   H " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 9 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L e g   #   B " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 1 0 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S s t i r r u p \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ c o l u m n s . h o r i z o n t a l H e a d e r I t e m ( 1 1 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " V u / V n " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 0 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I D " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 1 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " b \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 2 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " h \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 3 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L - e n d \ n " 
 
 " g%� _ t o p " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 4 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L - e n d \ n " 
 
 " g%� _ b o t " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 5 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L - e n d \ n " 
 
 " L e g   # " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 6 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L - e n d \ n " 
 
 " S s t i r r u p \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 7 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R - e n d \ n " 
 
 " g%� _ t o p " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 8 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R - e n d \ n " 
 
 " g%� _ b o t " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 9 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R - e n d \ n " 
 
 " L e g   # " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ b e a m s . h o r i z o n t a l H e a d e r I t e m ( 1 0 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R - e n d \ n " 
 
 " S s t i r r u p \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 0 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I D " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 1 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " t w \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 2 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " l w \ n " 
 
 " [ c m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 3 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " g%� l " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 4 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " g%� t " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 5 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " d b \ n " 
 
 " [ m m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 6 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " d s t \ n " 
 
 " [ m m ] " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 7 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " c / l w " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 8 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " g%� c / f \ ' c " ) ) 
 
                 i t e m   =   s e l f . t b l _ d a t a _ d e s i g n _ w a l l s . h o r i z o n t a l H e a d e r I t e m ( 9 ) 
 
                 i t e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " B o u n d a r y \ n " 
 
 " E l e m e n t s " ) ) 
 
                 s e l f . b t n _ a c c e p t _ d e s i g n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A c c e p t   D e s i g n " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ d e s i g n _ r e s u l t s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e s i g n   R e s u l t s " ) ) 
 
                 s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o l u m n s   a n d   b e a m s   p l a s t i c   h i n g e   l e n g t h   l p " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " >   =   0 . 5 H < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " >   =   0 . 0 8 l   +   0 . 0 2 2 d < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > b < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > f < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > y   < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > ( P r i e s t l e y   a n d   P a r k ) < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ l p 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " >   =   0 . 0 5 l   +   0 . 1 d < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > b < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > f < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > y   < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > /   �� � f \ ' < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > c   < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > ( B e r r y ) < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . g b x _ c o l u m n s _ b e a m s _ p l a s t i c _ h i n g e _ w a l l s _ p l a s t i c . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l s   p l a s t i c   h i n g e   l e n g t h   l p " ) ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " >   =   0 . 2 l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > w < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > + 0 . 0 4 4 ( M / V )   ( P r i e s t l e y ) < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " >   =   0 . 2 l < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > w < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > + 0 . 0 5 ( M / V ) ( 1 - 1 . 5 P / ( f \ ' A < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > g < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > ) ) < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' a r i a l , s a n s - s e r i f \ ' ;   f o n t - s i z e : 1 0 p t ;   c o l o r : # 2 0 2 1 2 4 ;   b a c k g r o u n d - c o l o r : # f f f f f f ; \ " > �� � < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > 0 . 8 l < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > w < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' a r i a l , s a n s - s e r i f \ ' ;   f o n t - s i z e : 1 0 p t ;   c o l o r : # 2 0 2 1 2 4 ;   b a c k g r o u n d - c o l o r : # f f f f f f ;   v e r t i c a l - a l i g n : s u b ; \ " / > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > ( B o h l ) < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " >   =   0 . 2 7 l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > w < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > ( 1 - P / ( f < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u p e r ; \ " > \ ' < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > c < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > A < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > g < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > ) ) ( 1 - f < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > y < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > g%� < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > s h < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > / f \ ' < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > c < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > ) ( M / V / l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > w < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > ) < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u p e r ; \ " > 0 . 4 5 < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > ( K a z a z ) < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ w a l l s _ p l a s t i c _ h i n g e _ l e n g t h _ l p 4 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " > l < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > p < / s p a n > < s p a n   s t y l e = \ "   f o n t - s t y l e : i t a l i c ; \ " >   =   a v e r a g e   o f   t h e   a b o v e < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . g b x _ r a y l e i g h _ d a m p i n g _ m o d e l . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R a y l e i g h   d a m p i n g   m o d e l " ) ) 
 
                 s e l f . r b n _ a s c e _ 4 1 _ 1 7 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A S C E   4 1 - 1 7   ( 7 . 4 . 4 . 4 ) " ) ) 
 
                 s e l f . r b n _ b a s e d _ o n _ t 1 _ t 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " B a s e d   o n   T 1   a n d   T 3 " ) ) 
 
                 s e l f . l b l _ t a r g e t _ d a m p i n g _ r a t i o . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T a r g e t   d a m p i n g   r a t i o   ( % ) : " ) ) 
 
                 s e l f . l b l _ s t i f f n e s s _ m a t r i x . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S i t f f n e s s   m a t r i x " ) ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c u r r e n t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C u r r e n t " ) ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ i n i t i a l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n i t i a l " ) ) 
 
                 s e l f . r b n _ s t i f f n e s s _ m a t r i x _ c o m m i t t e d . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o m m i t t e d " ) ) 
 
                 s e l f . g b x _ j o i n t _ m o d e l . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " J o i n t   m o d e l " ) ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R a d i o B u t t o n " ) ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R a d i o B u t t o n " ) ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R a d i o B u t t o n " ) ) 
 
                 s e l f . r b n _ j o i n t _ m o d e l _ l i n e a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L i n e a r " ) ) 
 
                 s e l f . g b x _ m a t e r i a l _ r e g u l a r i z a t i o n . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M a t e r i a l   R e g u l a r i z a t i o n " ) ) 
 
                 s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ c o n c r e t e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o n c r e t e " ) ) 
 
                 s e l f . c h k _ m a t e r i a l _ r e g u r a l i z a t i o n _ c o n c r e t e _ s t e e l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S t e e l " ) ) 
 
                 s e l f . g b x _ s h e a r _ m o d e l _ w a l l . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S h e a r   m o d e l   w a l l " ) ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ l i n e a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L i n e a r " ) ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ w a l l _ n o n l i n e a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n l i n e a r " ) ) 
 
                 s e l f . g b x _ s t e e l _ m o d e l . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S t e e l   m o d e l " ) ) 
 
                 s e l f . r b n _ s t e e l _ m o d e l _ h y s t e r e t i c . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " H y s t e r e t i c " ) ) 
 
                 s e l f . r b n _ s t e e l _ m o d e l _ s t e e l _ m p f . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S t e e l M P F " ) ) 
 
                 s e l f . g b x _ e l e m e n t _ m o d e l _ w a l l . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " E l e m e n t   m o d e l   w a l l " ) ) 
 
                 s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ f o r c e _ b e a m _ c o l u m n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F o r c e   B e a m   C o l u m n " ) ) 
 
                 s e l f . r b n _ e l e m e n t _ m o d e l _ w a l l _ n v l e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M V L E M " ) ) 
 
                 s e l f . g b x _ s h e a r _ m o d e l _ f r a m e . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S h e a r   m o d e l   f r a m e " ) ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n e " ) ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ l i n e a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L i n e a r " ) ) 
 
                 s e l f . r b n _ s h e a r _ m o d e l _ f r a m e _ n o n l i n e a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n l i n e a r " ) ) 
 
                 s e l f . g b x _ i n f i l l _ m o d e l _ w a l l . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n f i l l   m o d e l   w a l l " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ b e a m s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " B e a m s : " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ c o l u m n s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o l u m n s : " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ w a l l _ w a l l s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l s : " ) ) 
 
                 s e l f . g b x _ i n f i l l _ m o d e l _ w a l l _ r o w 3 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n f i l l   m o d e l   w a l l " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ t w . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > t < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > w < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " >   ( m m ) : < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ c e n t r a l _ s t r u t _ a r e a . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > C e n t r a l   s t r u t   a r e a   ( % ) : < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n u m b e r s _ b a r e _ f r a m e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N u m b e r s   o f   b a r e   f r a m e : " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ f m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > f ,%$%< / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > m   < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " >   ( M P a ) : < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ e m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > E < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > m < / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " >   ( M P a ) : < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ i n f i l l _ m o d e l _ n o n l i n e a r _ 4 1 1 7 _ c . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > C   ( M P a ) : < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . r b n _ i n f i l l _ m o d e l _ n o n l i n e a r _ a s c e _ 4 1 1 7 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n l i n e a r   A S C E   4 1 - 1 7 " ) ) 
 
                 s e l f . r b n _ s p x _ i n f i l l _ m o d e l _ n o n l i n e a r _ m a n u a l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n l i n e a r   m a n u a l " ) ) 
 
                 s e l f . l b l _ n o n l i n e a r _ m a n u a l _ f m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " > f ,%$%< / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ;   v e r t i c a l - a l i g n : s u b ; \ " > m   l%U%< / s p a n > < s p a n   s t y l e = \ "   f o n t - f a m i l y : \ ' A r i a l \ ' ;   f o n t - s i z e : 1 0 p t ;   f o n t - s t y l e : i t a l i c ; \ " >   ( M P a ) : < / s p a n > < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . g b x _ o p e r a t i o n s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " O p e r a t i o n s " ) ) 
 
                 s e l f . l b l _ n u m b e r _ e l e m e n t s _ m a c r o _ f i b e r s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N u m b e r   o f   e l e m e n t s   m a c r o - f i b e r s   M V L E M : " ) ) 
 
                 s e l f . b t n _ c r e a t e _ n o n l i n e a r _ m o d e l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C r e a t e   N o n l i n e a r   M o d e l " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ n o n l i n e a r _ p a r a m e t e r s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n l i n e a r   P a r a m e t e r s " ) ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P u s h o v e r " ) ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 1 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " _ " ) ) 
 
                 s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t r i a n g u l a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L o a d   p a t t e r n " ) ) 
 
                 s e l f . r b n _ l o a d _ p a t t e r n _ t r i a n g u l a r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T r i a n g u l a r " ) ) 
 
                 s e l f . r b n _ l o a d _ p a t t e r n _ u n i f o r m . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " U n i f o r m " ) ) 
 
                 s e l f . l b l _ n o n l i n e a r _ a n a l y s i s _ t y p e _ a n a l y s i s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T y p e   o f   a n a l y s i s " ) ) 
 
                 s e l f . r a d i o B u t t o n _ 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F a s t " ) ) 
 
                 s e l f . r a d i o B u t t o n _ 4 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F o r c e d " ) ) 
 
                 s e l f . l b l _ d r i f t _ p l o t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D r i f t   t o   p l o t " ) ) 
 
                 s e l f . c h k _ d r i f t _ p l o t _ s d r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S D R " ) ) 
 
                 s e l f . c h k _ d r i f t _ p l o t _ r d r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R D R " ) ) 
 
                 s e l f . l b l _ a l p h a _ c u r v e s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A l p h a   c u r v e s : " ) ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p u s h o v e r _ c o l u m n 2 . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " _ " ) ) 
 
                 s e l f . l b l _ t a r g e t _ s t o r y _ d r i f t _ r a t i o . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T a r g e t   s t o r y   d r i f t   r a t i o : " ) ) 
 
                 s e l f . l b l _ n u m b e r _ s t e p s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N u m b e r   o f   s t e p s : " ) ) 
 
                 s e l f . l b l _ o u t p u t _ p u s h o v e r _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " O u t p u t   P u s h o v e r   f i l e : " ) ) 
 
                 s e l f . l b l _ t y p e _ c h a r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " T y p e   o f   c h a r t " ) ) 
 
                 s e l f . r b n _ p h p _ p l a s t i c _ r o t a t i o n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P H P   p l a s t i c   r o t a t i o n " ) ) 
 
                 s e l f . r b n _ a c c e p t a n c e _ c r i t e r i a _ a s c e _ 1 7 4 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A c c e p t a n c e   c r i t e r i a   A S C E - 1 7 - 4 1 " ) ) 
 
                 s e l f . b t n _ r u n _ p u s h o v e r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R u n   P u s h o v e r " ) ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ c s s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C S S " ) ) 
 
                 s e l f . l b l _ g r o u n d _ m o t i o n s _ d i r e c t o r y . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " G r o u n d   m o t i o n s   d i r e c t o r y : " ) ) 
 
                 s e l f . l b l _ o u t p u t _ c s s _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " O u p u t   C S S   f i l e : " ) ) 
 
                 s e l f . l b l _ i n t e n s i t y _ m e a s u r e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n t e n s i t y   m e a s u r e   ( I M ) : " ) ) 
 
                 s e l f . l b l _ s a v e _ h i s t o r y _ r e s u l t s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S a v e   h i s t o r y   r e s u l t s : " ) ) 
 
                 s e l f . b t n _ r u n _ c s s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R u n   C S S " ) ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ i d a . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I D A " ) ) 
 
                 s e l f . l b l _ i d a _ f i r s t _ i n t e n s i t y . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " F i r s t   i n t e n s i t y : " ) ) 
 
                 s e l f . l b l _ i d a _ h u n t i n g _ i n c r e m e n t _ s t e p . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " H u n t i n g   i n c r e m e n t   s t e p   ( g ) : " ) ) 
 
                 s e l f . l b l _ i d a _ d r i f t _ c a p a c i t y . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D r i f t   c a p a c i t y   ( % ) : " ) ) 
 
                 s e l f . l b l _ i d a _ m a x i m u m _ n u m b e r _ r u n s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " M a x i m u m   n u m b e r   o f   r u n s : " ) ) 
 
                 s e l f . l b l _ i d a _ s e i s m i c _ r e c o r d s _ l i s t _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S e i s m i c   r e c o r d s   l i s t   f i l e : " ) ) 
 
                 s e l f . l b l _ i d a _ o u t p u t _ i d a _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " O u t p u t   I D A   f i l e : " ) ) 
 
                 s e l f . l b l _ i d a _ i n t e n s i t y _ m e a s u r e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n t e n s i t y   m e a s u r e   ( I M ) : " ) ) 
 
                 s e l f . b t n _ r u n _ i d a d . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " R u n   I D A " ) ) 
 
                 s e l f . g b x _ n o n l i n e a r _ a n a l y s i s _ p e r i o d s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P e r i o d s " ) ) 
 
                 s e l f . l b l _ t 1 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > T < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > 1   < / s p a n > : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ t 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > T < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > 2   < / s p a n > : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ t 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > T < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > 3   < / s p a n > : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ p e r i o d s _ a f t e r _ g r a v i t y _ l o a d s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P e r i o d s   a f t e r   g r a v i t y   l o a d s " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ n o n l i n e a r _ a n a l y s i s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " N o n l i n e a r   A n a l y s i s " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ p u s h o v e r _ r e s u l t s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P u s h o v e r   R e s u l t s " ) ) 
 
                 s e l f . l b l _ i n p u t _ i d a _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n p u t   I D A   f i l e : " ) ) 
 
                 s e l f . l b l _ s d r _ m a x _ c u r v e s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S D R   m a x   C u r v e s : " ) ) 
 
                 s e l f . b t n _ i d a _ r e s u l t s _ p l o t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P l o t " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ i d a _ r e s u l t s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I D A   R e s u l t s " ) ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ i n p u t _ c s s _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n p u t   C S S   f i l e : " ) ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ c h o o s e _ f a b i l i t y _ c u r v e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C h o o s e   F r a g i l i t y   C u r v e : " ) ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ l i m i t _ s t a g e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L i m i t   s t a g e   % : " ) ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ h a z a r d _ l e v e l _ p l o t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " H a z a r d   L e v e l   t o   p l o t : " ) ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ t m i n . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > t < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > m i n   < / s p a n > ( % ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l b l _ c s s _ r e s u l t s _ t d r . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S D R   % : " ) ) 
 
                 s e l f . b t n _ c s s _ r e s u l t s _ p l o t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P l o t " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ c s s _ r e s u l t s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C S S   R e s u l t s " ) ) 
 
                 s e l f . l a b e l . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I n p u t   C S S   f i l e : " ) ) 
 
                 s e l f . l a b e l _ 2 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " H a z a r d   L e v e l   t o   p l o t : " ) ) 
 
                 s e l f . l a b e l _ 3 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " < h t m l > < h e a d / > < b o d y > < p > t < s p a n   s t y l e = \ "   v e r t i c a l - a l i g n : s u b ; \ " > m i n   < / s p a n > ( % ) : < / p > < / b o d y > < / h t m l > " ) ) 
 
                 s e l f . l a b e l _ 4 . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " S D R   % : " ) ) 
 
                 s e l f . b t n _ p l o t _ c s s _ m a x _ f l o o r s . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " P l o t " ) ) 
 
                 s e l f . t w d _ p r i n c i p a l . s e t T a b T e x t ( s e l f . t w d _ p r i n c i p a l . i n d e x O f ( s e l f . t a b _ c s s _ g r a p h s ) ,   _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C S S   G r a p h s " ) ) 
 
                 s e l f . m n u _ f i l e . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A r c h i v o " ) ) 
 
                 s e l f . m n u _ a y u d a . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A y u d a " ) ) 
 
                 s e l f . m n u _ d e s i g n _ r e s u l t s . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " D e s i g n   R e s u l t s " ) ) 
 
                 s e l f . m n u _ b e a m _ d a t a . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " B e a m   d a t a " ) ) 
 
                 s e l f . m n u _ c o l u m n _ d a t a . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " C o l u m n   d a t a " ) ) 
 
                 s e l f . m n u _ w a l l _ d a t a . s e t T i t l e ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " W a l l   d a t a   f r o m   E x c e l . . . " ) ) 
 
                 s e l f . m n i _ l o a d _ f i l e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " L o a d   f i l e . . . " ) ) 
 
                 s e l f . m n i _ e x i t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " E x i t " ) ) 
 
                 s e l f . m n i _ a c e r c a _ d e . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " A c e r c a   d e . . . " ) ) 
 
                 s e l f . m n i _ b e a m _ d a t a _ i m p o r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I m p o r t   f r o m   E x c e l . . . " ) ) 
 
                 s e l f . m n i _ b e a m _ d a t a _ e x p o r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " E x p o r t   t o   E x c e l . . . " ) ) 
 
                 s e l f . m n i _ c o l u m n _ d a t a _ e x p o r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " E x p o r t   t o   E x c e l . . . " ) ) 
 
                 s e l f . m n i _ c o l u m n _ d a t a _ i m p o r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I m p o r t   f r o m   E x c e l . . . " ) ) 
 
                 s e l f . m n i _ w a l l _ d a t a _ i m p o r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " I m p o r t   f r o m   E x c e l . . . " ) ) 
 
                 s e l f . m n i _ w a l l _ d a t a _ e x p o r t . s e t T e x t ( _ t r a n s l a t e ( " N o n L i n e a r M a i n W i n d o w " ,   " E x p o r t   t o   E x c e l . . . " ) ) 
 
 f r o m   m p l w i d g e t   i m p o r t   M p l W i d g e t 
 
 