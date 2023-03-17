#! /bin/bash

rm -r $1/packages/{core-node,editor-codemirror,editor-server,editor-ui,eslint-config-custom-server,ojs,quarto-core,ui-widgets}
rm -r $1/apps/{lsp,vscode,vscode-editor,writer,writer-server}
patch -d $1 -p1 < $2
sed -i "s/\"esbuild\":.*/\"esbuild\": \"$(esbuild --version)\",/g" $1/packages/build/package.json
