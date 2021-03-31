%global bundled_gwt_version         2.8.2
%global bundled_websockets_version  1.0.4
%global bundled_gin_version         2.1.2
%global bundled_elemental2_version  1.0.0
%global bundled_junit_version       4.9b3
%global bundled_guice_version       3.0
%global bundled_corejs_version      3.6.4
%global bundled_aopalliance_version 1.0
%global bundled_rapidjson_version   5cd62c2
%global bundled_treehh_version      2.81
%global bundled_sundown_version     1.16.0
%global bundled_hunspell_version    1.3
%global bundled_synctex_version     1.17
%global bundled_gsllite_version     0.34.0
%global bundled_ace_version         1.4.5
%global bundled_datatables_version  1.10.4
%global bundled_jquery_version      3.5.1
%global bundled_pdfjs_version       1.3.158
%global bundled_revealjs_version    2.4.0
%global bundled_jsbn_version        1.1
%global bundled_highlightjs_version c589dcc
%global bundled_qunitjs_version     1.18.0
%global bundled_xtermjs_version     3.14.5
%global bundled_inertpol_version    0.2.5
%global bundled_focusvis_version    5.0.2
%global mathjax_short               27
%global rstudio_visual_editor       panmirror-0.1.0
%global rstudio_version_major       1
%global rstudio_version_minor       4
%global rstudio_version_patch       1106
%global rstudio_git_revision_hash   2389bc246c7946a8eb2f1a14e5a822bd5f6e1159

Name:           rstudio
Version:        %{rstudio_version_major}.%{rstudio_version_minor}.%{rstudio_version_patch}
Release:        3%{?dist}
Summary:        RStudio base package

# AGPLv3:       RStudio, hunspell, tree.hh
# LGPLv2+:      Stan Ace Mode
# ASL 2.0:      gwt, gwt-websockets, gin, guice, pdf.js, fast-text-encoding
# ASL 2.0:      inert-polyfill.js, elemental2
# MIT:          synctex, datatables, jquery, reveal.js, qunit.js, core-js
# MIT:          xterm.js, guidelines-support-library-lite, JSCustomBadge
# MIT:          ansi-regex, gsl-lite, ProseMirror, CodeMirror, OrderedMap
# MIT:          Clipboard.js, tlite
# BSD:          jsbn, ace, highlight.js
# ISC:          sundown
# W3C:          focus-visible.js
# MPLv1.1:      rhino
# CPL:          JUnit
# CC-BY:        a few icomoon glyphs
# Public:       aopalliance
License:        AGPLv3 and LGPLv2+ and ASL 2.0 and MIT and BSD and ISC and W3C and MPLv1.1 and CPL and CC-BY and Public Domain
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Node dependencies to build visual editor (use nodejs-bundler.sh)
Source1:        %{rstudio_visual_editor}-nm.tgz
Source2:        %{rstudio_visual_editor}-bundled-licenses.txt
Source3:        %{name}.metainfo.xml
# Unbundle mathjax, pandoc, hunspell dictionaries, qtsingleapplication
Patch0:         0000-unbundle-dependencies-common.patch
Patch1:         0001-unbundle-qtsingleapplication.patch
# Remove the installation prefix from the exec path in the .desktop file
Patch2:         0002-fix-rstudio-exec-path.patch
# We don't want to set RSTUDIO_PACKAGE_BUILD
Patch3:         0003-fix-resources-path.patch
# Use system-provided nodejs binary
Patch4:         0004-use-system-node.patch
# https://github.com/rstudio/rstudio/pull/8606
Patch5:         0005-fix-build-boost-175.patch

BuildRequires:  make, cmake, ant
BuildRequires:  gcc-c++, java-1.8.0-openjdk-devel, R-core-devel
BuildRequires:  nodejs-devel
BuildRequires:  pandoc, pandoc-citeproc
BuildRequires:  mathjax
BuildRequires:  lato-fonts, glyphography-newscycle-fonts
BuildRequires:  boost-devel
BuildRequires:  soci-postgresql-devel, soci-sqlite3-devel
BuildRequires:  rapidxml-devel
BuildRequires:  pam-devel
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(websocketpp)
BuildRequires:  pkgconfig(catch2)
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Suggests:       rstudio-desktop
%endif
Suggests:       rstudio-server
Recommends:     git
Requires:       hunspell
Requires:       pandoc, pandoc-citeproc
Requires:       mathjax
Requires:       lato-fonts, glyphography-newscycle-fonts

Provides:       bundled(gwt) = %{bundled_gwt_version}
Provides:       bundled(gwt-websockets) = %{bundled_websockets_version}
Provides:       bundled(gin) = %{bundled_gin_version}
Provides:       bundled(elemental2) = %{bundled_elemental2_version}
Provides:       bundled(junit) = %{bundled_junit_version}
Provides:       bundled(guice) = %{bundled_guice_version}
Provides:       bundled(nodejs-core-js) = %{bundled_corejs_version}
Provides:       bundled(aopalliance) = %{bundled_aopalliance_version}
Provides:       bundled(rapidjson-devel) = %{bundled_rapidjson_version}
Provides:       bundled(tree-hh-devel) = %{bundled_treehh_version}
Provides:       bundled(sundown) = %{bundled_sundown_version}
Provides:       bundled(hunspell) = %{bundled_hunspell_version}
Provides:       bundled(synctex) = %{bundled_synctex_version}
Provides:       bundled(guidelines-support-library-lite-devel) = %{bundled_gsllite_version}
Provides:       bundled(js-ace) = %{bundled_ace_version}
Provides:       bundled(js-datatables) = %{bundled_datatables_version}
Provides:       bundled(js-jquery) = %{bundled_jquery_version}
Provides:       bundled(js-pdf) = %{bundled_pdfjs_version}
Provides:       bundled(js-reveal) = %{bundled_revealjs_version}
Provides:       bundled(js-bn) = %{bundled_jsbn_version}
Provides:       bundled(js-highlight) = %{bundled_highlightjs_version}
Provides:       bundled(js-qunit) = %{bundled_qunitjs_version}
Provides:       bundled(js-xterm) = %{bundled_xtermjs_version}
Provides:       bundled(js-inert-polyfill) = %{bundled_inertpol_version}
Provides:       bundled(js-focus-visible) = %{bundled_focusvis_version}

%global _description %{expand:
RStudio is an integrated development environment (IDE) for R. It includes a
console, syntax-highlighting editor that supports direct code execution, as
well as tools for plotting, history, debugging and workspace management.
}

%description %_description
This package provides common files for %{name}-desktop and %{name}-server.

%ifarch %{qt5_qtwebengine_arches}
%package        desktop
Summary:        Integrated development environment for the R programming language
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme, shared-mime-info

%description    desktop %_description
This package provides the Desktop version, to access the RStudio IDE locally.
%endif

%package        server
Summary:        Access RStudio via a web browser
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(pre):  shadow-utils
%{?systemd_requires}

%description    server %_description
This package provides the Server version, a browser-based interface to the RStudio IDE.

%prep
%autosetup -p1
tar -xf %{SOURCE1}
mkdir src/gwt/panmirror/src/editor/node_modules
cp -r node_modules_prod/* src/gwt/panmirror/src/editor/node_modules
cp -r node_modules_dev/* src/gwt/panmirror/src/editor/node_modules
cp %{SOURCE2} .

# use system libraries when available
rm -rf src/cpp/desktop/3rdparty src/cpp/ext/websocketpp
ln -sf %{_includedir}/rapidxml.h src/cpp/core/include/core/rapidxml/rapidxml.hpp
ln -sf %{_includedir}/websocketpp src/cpp/ext/websocketpp
rm -rf src/cpp/tests/cpp/tests/vendor
ln -sf %{_includedir}/catch2 src/cpp/tests/cpp/tests/vendor

# don't include gwt_build in ALL to avoid recompilation
sed -i 's@gwt_build ALL@gwt_build@g' src/gwt/CMakeLists.txt
# increase Java stack size
%ifarch s390 s390x
sed -i '/StackOverflowError/c\<jvmarg value="-Xss8M"/>' src/gwt/build.xml
%endif

%build
export RSTUDIO_VERSION_MAJOR=%{rstudio_version_major}
export RSTUDIO_VERSION_MINOR=%{rstudio_version_minor}
export RSTUDIO_VERSION_PATCH=%{rstudio_version_patch}
export RSTUDIO_GIT_REVISION_HASH=%{rstudio_git_revision_hash}
export GIT_COMMIT=%{rstudio_git_revision_hash}
export PACKAGE_OS=$(cat /etc/redhat-release)
%cmake -B build \
%ifarch %{qt5_qtwebengine_arches}
    -DRSTUDIO_TARGET=Desktop \
    -DRSTUDIO_SERVER=TRUE \
    -DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt5 \
%else
    -DRSTUDIO_TARGET=Server \
%endif
    -DCMAKE_BUILD_TYPE=Release \
    -DRSTUDIO_USE_SYSTEM_SOCI=Yes \
    -DRSTUDIO_USE_SYSTEM_BOOST=Yes \
    -DBOOST_ROOT=%{_prefix} -DBOOST_LIBRARYDIR=%{_lib} \
    -DCMAKE_INSTALL_PREFIX=%{_libexecdir}/%{name}
%make_build -C build # ALL
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
%make_build -C build gwt_build

%install
%make_install -C build
# expose symlinks in /usr/bin
install -d -m 0755 %{buildroot}%{_bindir}
%ifarch %{qt5_qtwebengine_arches}
ln -s %{_libexecdir}/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}
%endif
for bin in %{name}-server rserver rserver-pam; do
    ln -s %{_libexecdir}/%{name}/bin/${bin} %{buildroot}%{_bindir}/${bin}
done

# validate .desktop and .metainfo.xml files
%ifarch %{qt5_qtwebengine_arches}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -m 0644 %{SOURCE3} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%endif

# create required directories for rstudio-server (according to INSTALL)
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}-server

# install the systemd service file and change /var/run -> /run
install -D -m 0644 \
    %{buildroot}%{_libexecdir}/%{name}/extras/systemd/%{name}-server.service \
    %{buildroot}%{_unitdir}/%{name}-server.service
sed -i 's@/var/run@/run@g' %{buildroot}%{_unitdir}/%{name}-server.service

# install the PAM module
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -m 0644 \
    %{buildroot}%{_libexecdir}/%{name}/extras/pam/%{name} \
    %{buildroot}%{_sysconfdir}/pam.d/%{name}

# symlink the location where the bundled dependencies should be
pushd %{buildroot}%{_libexecdir}/%{name}/bin
    mkdir -p pandoc
    ln -sf %{_bindir}/pandoc pandoc/pandoc
    ln -sf %{_bindir}/pandoc-citeproc pandoc/pandoc-citeproc
popd
pushd %{buildroot}%{_libexecdir}/%{name}/resources
    ln -sf %{_datadir}/myspell dictionaries
    ln -sf %{_datadir}/javascript/mathjax mathjax-%{mathjax_short}
    pushd presentation/revealjs/fonts
        for fnt in Lato*.ttf; do
            ln -sf %{_datadir}/fonts/lato/${fnt} ${fnt}
        done
        for fnt in News*.ttf; do
            ln -sf %{_datadir}/fonts/glyphography-newscycle-fonts/${fnt,,} ${fnt}
        done
    popd
    # move and symlink bundled libraries
    mv grid/datatables grid/datatables.bundled
    ln -sf ./datatables.bundled grid/datatables
    mv pdfjs pdfjs.bundled
    ln -sf ./pdfjs.bundled pdfjs
    mv presentation/revealjs presentation/revealjs.bundled
    ln -sf ./revealjs.bundled presentation/revealjs
popd

# clean up
pushd %{buildroot}%{_libexecdir}/%{name}
    for f in .gitignore .Rbuildignore LICENSE README; do
        find . -name ${f} -delete
    done
    rm -rf {extras,INSTALL,COPYING,NOTICE,README.md,SOURCE,VERSION}
popd

# add user rstudio-server
%pre server
getent group %{name}-server >/dev/null || groupadd -r %{name}-server
getent passwd %{name}-server >/dev/null || \
    useradd -r -g %{name}-server -d %{_sharedstatedir}/%{name}-server -s /sbin/nologin \
    -c "User for %{name}-server" %{name}-server
exit 0

%post server
%systemd_post %{name}-server.service

%preun server
%systemd_preun %{name}-server.service

%postun server
%systemd_postun_with_restart %{name}-server.service

%triggerun server -- %{name}-server
chown -R %{name}-server:%{name}-server %{_sharedstatedir}/%{name}-server

%files
%license COPYING NOTICE %{rstudio_visual_editor}-bundled-licenses.txt
%doc README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/R
%dir %{_libexecdir}/%{name}/bin
%{_libexecdir}/%{name}/bin/pandoc
%{_libexecdir}/%{name}/bin/postback
%{_libexecdir}/%{name}/bin/r-ldpath
%{_libexecdir}/%{name}/bin/rpostback
%{_libexecdir}/%{name}/bin/rsession
%{_libexecdir}/%{name}/resources
%{_libexecdir}/%{name}/www
%{_libexecdir}/%{name}/www-symbolmaps

%ifarch %{qt5_qtwebengine_arches}
%files desktop
%{_bindir}/%{name}
%{_libexecdir}/%{name}/%{name}.png
%{_libexecdir}/%{name}/bin/diagnostics
%{_libexecdir}/%{name}/bin/%{name}
%{_libexecdir}/%{name}/bin/%{name}-backtrace.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%endif

%files server
%{_bindir}/%{name}-server
%{_bindir}/rserver
%{_bindir}/rserver-pam
%{_libexecdir}/%{name}/bin/crash-handler-proxy
%{_libexecdir}/%{name}/bin/rserver
%{_libexecdir}/%{name}/bin/rserver-pam
%{_libexecdir}/%{name}/bin/%{name}-server
%dir %{_libexecdir}/%{name}/db
%{_libexecdir}/%{name}/db/20200226141952248123456_AddRevokedCookie.sql
%dir %{_sharedstatedir}/%{name}-server
%{_unitdir}/%{name}-server.service
%config(noreplace) %{_sysconfdir}/pam.d/%{name}

%changelog
* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.1106-3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.1106-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sat Feb 27 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1106-1
- Update to 1.4.1106

* Wed Feb 17 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1103-4
- Add metainfo.xml file (#1928992)
- Fix /var/lib/rstudio-server ownership

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.1103-2
- Rebuilt for Boost 1.75

* Sat Jan 16 2021 Iñaki Úcar <iucar@fedoraproject.org> - 1.4.1103-1
- Update to 1.4.1103

* Mon Nov 30 2020 Iñaki Úcar <iucar@fedoraproject.org> 1.3.1093-3
- https://fedoraproject.org/wiki/Changes/Remove_make_from_BuildRoot

* Wed Nov 11 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.1093-2
- Fix resources path for release build without RSTUDIO_PACKAGE_BUILD set

* Sat Sep 19 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.1093-1
- Update to 1.3.1093

* Wed Aug 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.1073-1
- Update to 1.3.1073

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1056-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1056-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.1056-2
- Rebuilt for JDK-11, attempt 2. see
  https://fedoraproject.org/wiki/Changes/Java11

* Wed Jul 15 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.1056-1
- Update to 1.3.1056

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.3.959-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jul 03 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.959-3
- Set PACKAGE_OS env variable
- Move to out-of-source build

* Tue Jun 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.959-2
- Add R-rmarkdown to Recommends
- Fix some bundled versions and licenses

* Sat May 30 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.3.959-1
- Update to 1.3.959
- Bump gwt version; gwt and gin are now included in the main source
- Bump MathJax version (now matches the one shipped in Fedora)
- Provide bundled rapidjson (devel version, not in Fedora); drop json-spirit
- Provide bundled guidelines-support-library-lite
- Provide bundled Ace (it was present before, but missing in Provides)
- Drop patches already merged upstream; rebase other patches
- Add new binary crash-handler-proxy to rstudio-server

* Sat May 30 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5042-5
- Fix compatibility with boost 1.73

* Tue May 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5042-4
- More granularity in file ownership under bin, sanitize requires

* Wed May 06 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5042-3
- Depend specifically on java-1.8.0-openjdk-devel
- Export JAVA_HOME to point to java-1.8.0

* Wed Apr 29 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5042-1
- Update to 1.2.5042, which adds support for R 4.0

* Mon Apr 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-14
- Use bundled jQuery before js-query is retired

* Mon Apr 06 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-13
- Remove unneeded qt5-devel metapackage dependency

* Thu Mar 19 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-12
- Add QT_QPA_PLATFORM=xcb to the desktop file to workaround Wayland issues

* Mon Mar 09 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-11
- Cleanup some old dependencies

* Fri Feb 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-10
- Do not remove NOTICE from resources dir (displayed in the help menu)

* Thu Feb 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-9
- Unbundle NewsCycle font
- Make unzip quiet
- Simplify description

* Tue Feb 25 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-8
- Explicitly list gcc-c++ and java-devel as BuildRequires
- Change Source0 URL to include the package name
- Add isa flag to subpackages
- Require hicolor-icon-theme and shared-mimo-info in -desktop
- Mark config file as noreplace in -server
- Add comments to justify patches
- Unbundle Lato font
- Some refactoring

* Sun Feb 23 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-7
- Downgrade to gwt version 2.8.1 to fix notebook issues
- Rebase patches

* Fri Feb 21 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-6
- Declare bundled hunspell, synctex (RStudio relies on an old APIs)

* Thu Feb 20 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-5
- Declare bundled gwt-websockets, guice, aopalliance, json-spirit, sundown,
  datatables, pdfjs, revealjs, jsbn, highlightjs, qunitjs
- Move and symlink bundled libraries included as-is: datatables, pdfjs, revealjs
- Unbundle qtsingleapplication, websocketpp, hunspell, dictionaries, rapidxml,
  synctex, jQuery
- Validate .desktop file
- Expose rstudio-server script in /usr/bin
- Mark NOTICE as license, clean up more files
- Rebase patches

* Mon Feb 17 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-4
- Increase Java stack size for s390x
- Call target gwt_build manually

* Sun Feb 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-3
- Move PNG file to rstudio-desktop sub-package

* Sun Feb 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-2
- Exclude rstudio-desktop from arches not supported by QtWebEngine
- Add 0004-fix-STL-access-undefined-behaviour.patch

* Sun Feb 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5033-1
- Initial packaging for Fedora
- Most of the work ported from Dan Čermák's SPEC for openSUSE
