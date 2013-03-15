Summary: Recompression utilities for .PNG, .MNG and .ZIP files
Name: advancecomp
Version: 1.15
Release: 18%{?dist}
License: GPLv2+
Group: Applications/Emulators
URL: http://advancemame.sourceforge.net/
Source: http://downloads.sf.net/advancemame/advancecomp-%{version}.tar.gz
BuildRequires: zlib-devel

%description
AdvanceCOMP is a set of recompression utilities for .PNG, .MNG and .ZIP files.
The main features are :
* Recompress ZIP, PNG and MNG files using the Deflate 7-Zip implementation.
* Recompress MNG files using Delta and Move optimization.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING HISTORY README
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.15-16
- Add disttag, modernise spec file

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-15
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.15-10
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.15-9
- Rebuild for new BuildID feature.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 1.15-8
- Update License field.
- Remove dist tag, since the package will seldom change.

* Thu Mar 29 2007 Matthias Saou <http://freshrpms.net/> 1.15-7
- Switch to using DESTDIR install method.

* Thu Mar 29 2007 Matthias Saou <http://freshrpms.net/> 1.15-6
- Switch to use downloads.sf.net source URL.
- Tweak defattr.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.15-5
- FC6 rebuild, remove gcc-c++ build requirement (it's a default).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.15-4
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 1.15-3
- Rebuild for new gcc/glibc.

* Tue Jan 24 2006 Matthias Saou <http://freshrpms.net/> 1.15-2
- Rebuild for FC5.

* Wed Nov  2 2005 Matthias Saou <http://freshrpms.net/> 1.15-1
- Update to 1.15, includes 64bit fixes.

* Fri May 27 2005 Matthias Saou <http://freshrpms.net/> 1.14-5
- Update 64bit patch to a cleaner approach as Ralf suggested.

* Thu May 26 2005 Jeremy Katz <katzj@redhat.com> - 1.14-4
- fix build on 64bit arches

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.14-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.14-2
- rebuilt

* Wed Feb 23 2005 Matthias Saou <http://freshrpms.net/> 1.14-1
- Update to 1.14.

* Mon Nov 29 2004 Matthias Saou <http://freshrpms.net/> 1.13-1
- Update to 1.13.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 1.12-1
- Update to 1.12.

* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net/> 1.11-1
- Update to 1.11.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 1.10-1
- Update to 1.10.

* Mon Nov  3 2003 Matthias Saou <http://freshrpms.net/> 1.7-2
- Rebuild for Fedora Core 1.
- Added missing build dependencies, thanks to mach.

* Tue Aug 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7.

* Thu May 22 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

