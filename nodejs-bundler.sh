#!/bin/bash

usage() {
  echo "Usage `basename $0` <path>" >&2
  echo >&2
  echo "  Given a npm module path, download dependencies," >&2
  echo "    each in their own tarball." >&2
  echo "    Also finds licenses prod dependencies." >&2
  echo >&2
  exit 1
}

if ! [ -f /usr/bin/npm ]; then 
  echo >&2
  echo "`basename $0` requires npm to run" >&2
  echo >&2
  echo "Run the following to fix this" >&2
  echo "  sudo dnf install npm" >&2
  echo >&2
  exit 2
fi 

if [ $# -lt 1 ]; then 
  usage
else
  case $1 in
	  -h | --help )
		  usage
		;;
		* )
		  PACKAGE="$1"
		;;
	esac
fi

download_deps () {
  PACKAGE_DIR=$(tar tf $PACKAGE | head -n1)
  tar xf $PACKAGE
  ./panmirror-cleanup.sh $PACKAGE_DIR panmirror-cleanup.patch

  APP=apps/panmirror
  NAME=$(jq -r .name ${PACKAGE_DIR}/$APP/package.json)
  VERSION=$(jq -r .version ${PACKAGE_DIR}/$APP/package.json)

  pushd ${PACKAGE_DIR}
    echo " Downloading $1 dependencies..."
    [ "$1" = "prod" ] && YARN_FLAG="--prod" || YARN_FLAG=""
    yarn install --ignore-optional $YARN_FLAG
    status=$?
  popd

  if [ ${status} -ge 1 ] ; then
    echo "    ERROR WILL ROBINSON"
    rm -rf ${PACKAGE_DIR}
    exit 1
  fi

  rm -rf ${PACKAGE_DIR}/node_modules/esbuild-linux*
  rm -rf ${PACKAGE_DIR}/node_modules/vite/node_modules
  mv ${PACKAGE_DIR}/node_modules node_modules_$1
  rm -rf ${PACKAGE_DIR}
}

download_deps prod

echo " Licenses in bundle..."
LICENSES="${NAME}-${VERSION}-bundled-licenses.txt"
find node_modules* -name "package.json" -exec jq -r .license {} \; > ${LICENSES}
find node_modules* -name "package.json" -exec jq -r '.licenses[] .type' {} \; \
  >> ${LICENSES} 2>/dev/null
sed -i "/^null$/d" ${LICENSES}
sort -u -o ${LICENSES} ${LICENSES}
echo " Done. Please, check ${LICENSES} and remove the garbage."

download_deps dev

tar cfz ${NAME}-${VERSION}-nm.tgz node_modules_*
rm -rf node_modules_*
