
language messages C
set nu showcmd
syntax on
filetype indent on
set et
set sw=4
set ts=4
set autoindent
set smarttab

set showmatch
set hlsearch
set incsearch
"set ignorecase
set listchars=tab:..
set list

set ffs=unix,dos,mac
set fencs=utf-8
set encoding=utf-8
set langmap=йq,цw,уe,кr,еt,нy,гu,шi,щo,зp,х[,ъ],фa,ыs,вd,аf,пg,рh,оj,лk,дl,э',яz,чx,сc,мv,иb,тn,ьm,ЙQ,ЦW,УE,КR,ЕT,НY,ГU,ШI,ЩO,ЗP,Х[,Ъ],ФA,ЫS,ВD,АF,ПG,РH,ОJ,ЛK,ДL,Э',ЯZ,ЧX,СC,МV,ИB,ТN,ЬM

map <Up> gk
map <Down> gj

if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

au FileType make set noet
au FileType go set noet
au FileType proto set sw=2 ts=2

match ErrorMsg /\%<81v.\%>77v/
2match ErrorMsg /\s\+$/

" vim -b : edit binary using xxd-format!
augroup Binary
  au!
  au BufReadPre  *.bin let &bin=1
  au BufReadPost *.bin if &bin | %!xxd
  au BufReadPost *.bin set ft=xxd | endif
  au BufWritePre *.bin if &bin | %!xxd -r
  au BufWritePre *.bin endif
  au BufWritePost *.bin if &bin | %!xxd
  au BufWritePost *.bin set nomod | endif
augroup END

autocmd BufNewFile,BufReadPost *.md set filetype=markdown

set undodir=~/.vim/undodir
set undofile
set undolevels=1000 "maximum number of changes that can be undone
set undoreload=10000 "maximum number lines to save for undo on a buffer reload
