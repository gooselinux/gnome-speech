%define po_package gnome-speech

Summary: GNOME Text to Speech
Name: gnome-speech
Version: 0.4.25
Release: 3.1%{?dist}
License: LGPLv2+
Group: Desktop/Accessibility
URL: http://www.gnome.org/
Source0: http://download.gnome.org/sources/gnome-speech/0.4/gnome-speech-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
BuildRequires: pkgconfig
BuildRequires: autoconf, automake, gettext, libtool
BuildRequires: libbonobo-devel
BuildRequires: espeak-devel
Patch1: gnome-speech-0.3.5-no-gnome-common.patch
Patch2: gnome-speech-0.4.18-dont-fail.patch
Requires: festival >= 1.96-0.11

%description
The GNOME Speech library provides a simple general API for 
producing text-to-speech output.


%package devel
Summary:	The files needed for developing an app using gnome-speech
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbonobo-devel
Requires:	pkgconfig

%description devel
The gnome-speech-devel package contains files needed for developing
applications using GNOME Speech.


%package espeak
Summary:	gnome-speech driver for eSpeak
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description espeak
The gnome-speech-espeak package contains a driver for using GNOME Speech
with eSpeak.


%prep
%setup -q
%patch1 -p1 -b .no-gnome-common
%patch2 -p1 -b .dont-fail

%build
autoreconf -f -i
%configure --with-java-home=no --with-jab-dir="" --with-espeak-dir=""
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

find $RPM_BUILD_ROOT -name '*.la' |xargs /bin/rm
# Remove this as it does not build correctly right now.

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/test-speech
%{_libdir}/lib*.so.*
%{_libdir}/orbit-2.0/*.so
%{_bindir}/festival-synthesis-driver
%{_libdir}/bonobo/servers/GNOME_Speech_SynthesisDriver_Festival.server

%files devel
%defattr(-,root,root,-)
%doc doc/gnome-speech.html
%{_libdir}/lib*.so
%{_includedir}/gnome-speech-1.0
%{_libdir}/pkgconfig/*pc
%{_datadir}/idl/gnome-speech-1.0

%files espeak
%defattr(-,root,root,-)
%{_bindir}/espeak-synthesis-driver
%{_libdir}/bonobo/servers/GNOME_Speech_SynthesisDriver_Espeak.server


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4.25-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.25-1
- Update to 0.4.25

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.23-1
- Update to 0.4.23

* Sun Aug  3 2008 Matthias Clasen <mclasen@redhat.com> - 0.4.21-1
- Update to 0.4.21

* Wed Jul 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.20-2
- fix license tag

* Wed Jun 18 2008  Matthias Clasen <mclasen@redhat.com> - 0.4.20-1
- Update to 0.4.20

* Fri Apr 25 2008  Matthias Clasen <mclasen@redhat.com> - 0.4.19-1
- Update to 0.4.19

* Thu Apr 17 2008  Ray Strode <rstrode@redhat.com> - 0.4.18-3
- Don't crash in a normal failure case

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.18-2
- Autorebuild for GCC 4.3

* Mon Jan 14 2008  Matthias Clasen <mclasen@redhat.com> - 0.4.18-1
- Update to 0.4.18

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.4.16-2
- Rebuild for selinux ppc32 issue.

* Sun Jul 29 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.16-1
- Update to 0.4.16

* Tue Jul 24 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.15-2
- Build the espeak driver and put it in a subpackage

* Mon Jul  9 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.15-1
- Update to 0.4.15

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.14
- Update to 0.4.14

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.13
- Update to 0.4.13

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.12
- Update to 0.4.12

* Tue Mar 20 2007 David Zeuthen <davidz@redhat.com> - 0.4.10-2
- Drop i386-only requirement (#232517)
- Require newer version of festival

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.10-1
- Update to 0.4.10

* Sun Feb 11 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.9-1
- Update to 0.4.9 

* Sat Jan 20 2007 Matthias Clasen <mclasen@redhat.com> - 0.4.8-1
- Update to 0.4.8

* Wed Dec 20 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.7-1
- Update to 0.4.7
- Require pkgconfig in the -devel package

* Sun Nov  5 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.6-1
- Update to 0.4.6

* Tue Aug 29 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.5-1.fc6
- Update to 0.4.5

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.4-1.fc6
- Update to 0.4.4

* Fri Aug  4 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.2-1.fc6
- Update to 0.4.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.4.1-1.1
- rebuild

* Tue Jul 11 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.0-2
- Add missing BuildRequires

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Wed May 10 2006 Matthias Clasen <mclasen@redhat.com> - 0.3.10-1
- Update to 0.3.10

* Fri Feb 24 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.9-3
- Revert back to devel package and enable the bonobo build

* Thu Feb 23 2006 John (J5) Palmieri <johnp@redhat.com> - 0.3.9-2
- Get rid of devel package
- .so now available to bonobo

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.3.9-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.3.9-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec  2 2005 Matthias Clasen <mclasen@redhat.com> 0.3.9-1
- Update to 0.3.9

* Thu Oct  6 2005 Matthias Clasen <mclasen@redhat.com> 0.3.8-1
- Update to 0.3.8

* Fri Aug  5 2005 Matthias Clasen <mclasen@redhat.com> 0.3.7-1
- New upstream version

* Fri Jan 28 2005 Matthias Clasen <mclasen@redhat.com> 0.3.6-1
- Update to 0.3.6

* Tue Jan 04 2005 Colin Walters <walters@redhat.com> 0.3.5-5
- New patch gnome-speech-0.3.5-java-configure.patch to
  allow to explicitly disable Java
- Use it
- New patch gnome-speech-0.3.5-no-gnome-common.patch

* Thu Sep 16 2004 Jonathan Blandford <jrb@redhat.com> 0.3.5-4
- change ExclusiveArch to Requires festival only on i386

* Wed Sep 15 2004 Tim Powers <timp@redhat.com> 0.3.5-3
- ExclusiveArch i386 since festival only exists for i386, otherwise we break deps

* Tue Sep 14 2004 GNOME <jrb@redhat.com> - 0.3.5-2
- require festival, as we're useless without it

* Tue Aug 31 2004 Colin Walters <walters@redhat.com> 0.3.5-1
- Update to 0.3.5
- Add missing ldconfig calls (bz #123268)

* Wed Aug 04 2004 Colin Walters <walters@redhat.com> 0.3.3-1
- Update to 0.3.3

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Apr 10 2004 Warren Togami <wtogami@redhat.com> 0.3.2-2
- BR pkgconfig libbonobo-devel

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 0.3.2-1
- Update to 0.3.2

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 0.3.1-1
- update to 0.3.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Oct  2 2003 Jonathan Blandford <jrb@redhat.com> 0.2.7-1
- new version

* Tue Sep  2 2003 Jonathan Blandford <jrb@redhat.com>
- rebuild

* Mon Jul 28 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add defattr to devel subrpm

* Fri Jul 18 2003 Jonathan Blandford <jrb@redhat.com>
- remove non-working orbit-2.0 typelib stuff temporarily

* Thu Jul 17 2003 root <jrb@dhcp64-232.boston.redhat.com> 0.2.3-1
- bump to new version

* Fri May  9 2003 Jonathan Blandford <jrb@redhat.com> speech-1
- Initial build.


