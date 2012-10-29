Summary:	An abstract soundfile decoder
Name:		SDL_sound
Version:	1.0.3
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.icculus.org/SDL_sound/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	aa09cd52df85d29bee87a664424c94b5
URL:		http://www.icculus.org/SDL_sound/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libtool
BuildRequires:	smpeg-devel
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3. It is meant to make the
programmer's sound playback tasks simpler. The programmer gives
SDL_sound a filename, or feeds it data directly from one of many
sources, and then reads the decoded waveform data back at her leisure.
If resource constraints are a concern, SDL_sound can process sound
data in programmer-specified blocks. Alternately, SDL_sound can decode
a whole sound file and hand back a single pointer to the whole
waveform. SDL_sound can also handle sample rate, audio format, and
channel conversion on-the-fly and behind-the-scenes, if the programmer
desires.

%package devel
Summary:	Header files and more to develop SDL_sound applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and more to develop SDL_sound applications.

%prep
%setup -q

%build
rm acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains additional notes
%doc CHANGELOG COPYING CREDITS README TODO
%attr(755,root,root) %{_bindir}/playsound
%attr(755,root,root) %ghost %{_libdir}/libSDL_sound-1.0.so.?
%attr(755,root,root) %{_libdir}/libSDL_sound-1.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_sound.so
%{_libdir}/libSDL_sound.la
%{_includedir}/SDL/SDL_sound.h

