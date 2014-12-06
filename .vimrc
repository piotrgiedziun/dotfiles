set nocompatible
syntax on
colo peachpuff

" Tab between buffers
noremap <tab> <c-w>w
noremap <S-tab> <c-w>W

" Show the file name in the window title bar.
set title

" Enable line numbers.
set number
set relativenumber

" Show invisible characters.
set listchars=tab:▸\ ,trail:·
set list

" Enable mouse support for normal mode.
set mouse=n
set ttymouse=xterm2

" Disable error bells.
set noerrorbells visualbell t_vb=
augroup GUIBell
  autocmd!
  autocmd GUIEnter * set visualbell t_vb=
augroup END
