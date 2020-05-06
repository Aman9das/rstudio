%global bundled_gwt_version         2.8.1
%global bundled_websockets_version  1.0.4
%global bundled_gin_version         2.1.2
%global bundled_guice_version       3.0
%global bundled_aopalliance_version 1.0
%global bundled_jsonspirit_version  4.03
%global bundled_sundown_version     07d0d98
%global bundled_hunspell_version    1.3
%global bundled_synctex_version     1.17
%global bundled_datatables_version  1.10.4
%global bundled_jquery_version      3.4.0
%global bundled_pdfjs_version       1.3.158
%global bundled_revealjs_version    2.4.0
%global bundled_jsbn_version        2005
%global bundled_highlightjs_version c589dcc
%global bundled_qunitjs_version     1.18.0
%global bundled_xtermjs_version     0.0.7
%global mathjax_short               26
%global rstudio_version_major       1
%global rstudio_version_minor       2
%global rstudio_version_patch       5042
%global rstudio_git_revision_hash   e4a1c219cbf6c10d9aec41461d80171ab3009bef

Name:           rstudio
Version:        %{rstudio_version_major}.%{rstudio_version_minor}.%{rstudio_version_patch}
Release:        2%{?dist}
Summary:        RStudio base package

# AGPLv3:       RStudio, hunspell, icomoon glyphs
# ASL 2.0:      gwt, gwt-websockets, gin, guice, pdf.js
# MIT:          synctex, json-spirit, sundown, datatables, jquery, reveal.js,
#               jsbn, qunit.js, xterm.js
# BSD:          highlight.js
# Public:       aopalliance
License:        AGPLv3 and ASL 2.0 and MIT and BSD and Public Domain
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://s3.amazonaws.com/%{name}-buildtools/gwt-%{bundled_gwt_version}.zip
Source2:        https://s3.amazonaws.com/%{name}-buildtools/gin-%{bundled_gin_version}.zip
# Unbundle mathjax, pandoc, hunspell dictionaries, qtsingleapplication
Patch0:         0000-unbundle-dependencies-common.patch
Patch1:         0001-unbundle-qtsingleapplication.patch
# Remove the installation prefix from the exec path in the .desktop file
Patch2:         0002-fix-rstudio-exec-path.patch
# https://github.com/rstudio/rstudio/pull/6244
Patch3:         0003-fix-STL-access-undefined-behaviour.patch
# https://github.com/rstudio/rstudio/pull/6017
Patch4:         0004-fix-build-under-Rv4.0.patch

BuildRequires:  cmake, ant
BuildRequires:  gcc-c++, java-devel <= 1:1.8.0, R-core-devel
BuildRequires:  pandoc, pandoc-citeproc
BuildRequires:  mathjax
BuildRequires:  lato-fonts, glyphography-newscycle-fonts
BuildRequires:  boost-devel
BuildRequires:  pam-devel
BuildRequires:  rapidxml-devel
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(websocketpp)
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
%endif
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd
%{?systemd_requires}
Requires(pre):  shadow-utils
Requires:       hunspell
Requires:       pandoc, pandoc-citeproc
Requires:       mathjax
Requires:       lato-fonts, glyphography-newscycle-fonts
Recommends:     git
%ifarch %{qt5_qtwebengine_arches}
Suggests:       rstudio-desktop
%endif
Suggests:       rstudio-server
Provides:       bundled(gwt) = %{bundled_gwt_version}
Provides:       bundled(gwt-websockets) = %{bundled_websockets_version}
Provides:       bundled(gin) = %{bundled_gin_version}
Provides:       bundled(guice) = %{bundled_guice_version}
Provides:       bundled(aopalliance) = %{bundled_aopalliance_version}
Provides:       bundled(json-spirit) = %{bundled_jsonspirit_version}
Provides:       bundled(sundown) = %{bundled_sundown_version}
Provides:       bundled(hunspell) = %{bundled_hunspell_version}
Provides:       bundled(synctex) = %{bundled_synctex_version}
Provides:       bundled(js-datatables) = %{bundled_datatables_version}
Provides:       bundled(js-jquery) = %{bundled_jquery_version}
Provides:       bundled(js-pdf) = %{bundled_pdfjs_version}
Provides:       bundled(js-reveal) = %{bundled_revealjs_version}
Provides:       bundled(js-bn) = %{bundled_jsbn_version}
Provides:       bundled(js-highlight) = %{bundled_highlightjs_version}
Provides:       bundled(js-qunit) = %{bundled_qunitjs_version}
Provides:       bundled(js-xterm) = %{bundled_xtermjs_version}

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
Requires:       pam

%description    server %_description
This package provides the Server version, a browser-based interface to the RStudio IDE.

%prep
%autosetup -p1

# unpack gwt
mkdir -p src/gwt/lib/gwt
unzip -q -d src/gwt/lib/gwt/ %{SOURCE1}
mv src/gwt/lib/gwt/gwt-%{bundled_gwt_version} src/gwt/lib/gwt/%{bundled_gwt_version}
# unpack gin
mkdir -p src/gwt/lib/gin/%{bundled_gin_version}
unzip -q -d src/gwt/lib/gin/%{bundled_gin_version} %{SOURCE2}

# use system libraries when available
rm -rf src/cpp/desktop/3rdparty src/cpp/ext/websocketpp
ln -sf %{_includedir}/rapidxml.h src/cpp/core/include/core/rapidxml/rapidxml.hpp
ln -sf %{_includedir}/websocketpp src/cpp/ext/websocketpp

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
%cmake . \
%ifarch %{qt5_qtwebengine_arches}
    -DRSTUDIO_TARGET=Desktop \
    -DRSTUDIO_SERVER=TRUE \
    -DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt5 \
%else
    -DRSTUDIO_TARGET=Server \
%endif
    -DCMAKE_BUILD_TYPE=Release \
    -DRSTUDIO_USE_SYSTEM_BOOST=Yes \
    -DBOOST_ROOT=%{_prefix} -DBOOST_LIBRARYDIR=%{_lib} \
    -DCMAKE_INSTALL_PREFIX=%{_libexecdir}/%{name}
%make_build # ALL
%make_build gwt_build

%install
%make_install
# expose symlinks in /usr/bin
install -d -m 0755 %{buildroot}%{_bindir}
%ifarch %{qt5_qtwebengine_arches}
ln -s %{_libexecdir}/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}
%endif
for bin in %{name}-server rserver rserver-pam; do
    ln -s %{_libexecdir}/%{name}/bin/${bin} %{buildroot}%{_bindir}/${bin}
done

# validate .desktop file
%ifarch %{qt5_qtwebengine_arches}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
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

%files
%license COPYING NOTICE
%doc README.md
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/R
%{_libexecdir}/%{name}/bin
%{_libexecdir}/%{name}/resources
%{_libexecdir}/%{name}/www
%{_libexecdir}/%{name}/www-symbolmaps

%ifarch %{qt5_qtwebengine_arches}
%files desktop
%{_bindir}/%{name}
%{_libexecdir}/%{name}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%endif

%files server
%{_bindir}/%{name}-server
%{_bindir}/rserver
%{_bindir}/rserver-pam
%dir %{_sharedstatedir}/%{name}-server
%{_unitdir}/%{name}-server.service
%config(noreplace) %{_sysconfdir}/pam.d/%{name}

%changelog
* Wed May 06 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.2.5042-2
- Depend specifically on java-devel <= 1:1.8.0

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
