echo ++[. bashrc.steve]
  steve.sys.clone-manifest
. steve.sys:add-packages

. bh.monty:activate
  bh.vim.configure
. steve.path:clean
echo --[. bashrc.steve]

