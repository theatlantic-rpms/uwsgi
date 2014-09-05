# Version
%global majornumber 2
%global minornumber 0
%global releasenumber 6

# Documentation sources:
%global commit d2c4969e82c12b316889bcdce348d200b45c4a3e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global docrepo uwsgi-docs
%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Name:           uwsgi
Version:        %{majornumber}.%{minornumber}.%{releasenumber}%{?patchnumber}
Release:        0%{dist}
Summary:        Fast, self-healing, application container server
Group:          System Environment/Daemons   
License:        GPLv2 with exceptions
URL:            https://github.com/unbit/uwsgi
Source0:        http://projects.unbit.it/downloads/%{name}-%{version}.tar.gz
Source1:        fedora.ini
Source2:        uwsgi.service
Source3:        emperor.ini
Source4:        https://github.com/unbit/%{docrepo}/archive/%{commit}/%{docrepo}-%{shortcommit}.tar.gz
Source5:        README.Fedora
Patch0:         uwsgi_trick_chroot_rpmbuild.patch
Patch1:         uwsgi_fix_rpath.patch
Patch2:         uwsgi_ruby20_compatibility.patch
Patch3:         uwsgi_fix_lua.patch
BuildRequires:  curl,  python2-devel, libxml2-devel, libuuid-devel, jansson-devel
BuildRequires:  libyaml-devel, perl-devel, ruby-devel, perl-ExtUtils-Embed
BuildRequires:  python3-devel, python-greenlet-devel, lua-devel, ruby, pcre-devel
BuildRequires:  php-devel, php-embedded, libedit-devel, openssl-devel
BuildRequires:  bzip2-devel, gmp-devel, systemd-units, pam-devel
BuildRequires:  java-devel, sqlite-devel, libcap-devel, systemd-devel
BuildRequires:  httpd-devel, tcp_wrappers-devel, zeromq-devel, libcurl-devel
BuildRequires:  gloox-devel, perl-Coro, libstdc++-devel, libgo-devel, gcc-go
BuildRequires:  GeoIP-devel, libevent-devel, glusterfs-api-devel, zlib-devel
BuildRequires:  libmongodb-devel, mono-devel
Obsoletes:      %{name}-loggers <= 1.9.8-1
Obsoletes:      %{name}-routers <= 2.0.6
Obsoletes:      %{name}-plugin-erlang <= 1.9.20-1
Obsoletes:      %{name}-plugin-admin <= 2.0.6

Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

%description
uWSGI is a fast (pure C), self-healing, developer/sysadmin-friendly
application container server.  Born as a WSGI-only server, over time it has
evolved in a complete stack for networked/clustered web applications,
implementing message/object passing, caching, RPC and process management. 
It uses the uwsgi (all lowercase, already included by default in the Nginx
and Cherokee releases) protocol for all the networking/interprocess
communications.  Can be run in preforking mode, threaded,
asynchronous/evented and supports various form of green threads/co-routine
(like uGreen and Fiber).  Sysadmin will love it as it can be configured via
command line, environment variables, xml, .ini and yaml files and via LDAP. 
Being fully modular can use tons of different technology on top of the same
core.

%package -n %{name}-devel
Summary:  uWSGI - Development header files and libraries
Group:    Development/Libraries
Requires: %{name}

%description -n %{name}-devel
This package contains the development header files and libraries
for uWSGI extensions

%package -n %{name}-docs
Summary:  uWSGI - Documentation
Group:    Documentation
Requires: %{name}

%description -n %{name}-docs
This package contains the documentation files for uWSGI

%package -n %{name}-plugin-common
Summary:  uWSGI - Common plugins for uWSGI
Group:    System Environment/Daemons
Requires: %{name}

%description -n %{name}-plugin-common
This package contains the most common plugins used with uWSGI. The
plugins included in this package are: cache, CGI, RPC, uGreen

# Alarms

%package -n %{name}-alarm-curl
Summary:  uWSGI - Curl alarm plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libcurl


%description -n %{name}-alarm-curl
This package contains the alarm_curl alarm plugin for uWSGI

%package -n %{name}-alarm-xmpp
Summary:  uWSGI - Curl alarm plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, gloox

%description -n %{name}-alarm-xmpp
This package contains the alarm_xmpp alarm plugin for uWSGI

# Loggers

%package -n %{name}-log-encoder-msgpack
Summary:  uWSGI - msgpack log encoder plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-log-encoder-msgpack
This package contains the msgpack log encoder plugin for uWSGI

%package -n %{name}-logger-crypto
Summary:  uWSGI - logcrypto logger plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-logger-crypto
This package contains the logcrypto logger plugin for uWSGI

%package -n %{name}-logger-file
Summary:   uWSGI - logfile logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-loggers <= 1.9.8-1
Provides:  %{name}-loggers = %{version}-%{release}

%description -n %{name}-logger-file
This package contains the logfile logger plugin for uWSGI

%package -n %{name}-logger-graylog2
Summary:   uWSGI - Graylog2 logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common, zlib

%description -n %{name}-logger-graylog2
This package contains the graylog2 logger plugin for uWSGI

%package -n %{name}-logger-mongodb
Summary:   uWSGI - mongodblog logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-loggers <= 1.9.8-1
Provides:  %{name}-loggers = %{version}-%{release}

%description -n %{name}-logger-mongodb
This package contains the mongodblog logger plugin for uWSGI

%package -n %{name}-logger-pipe
Summary:  uWSGI - logpipe logger plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-logger-pipe
This package contains the logcrypto logger plugin for uWSGI

%package -n %{name}-logger-redis
Summary:   uWSGI - redislog logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-loggers <= 1.9.8-1
Provides:  %{name}-loggers = %{version}-%{release}

%description -n %{name}-logger-redis
This package contains the redislog logger plugin for uWSGI

%package -n %{name}-logger-rsyslog
Summary:   uWSGI - rsyslog logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-plugin-rsyslog <= 1.9.8-1
Provides:  %{name}-plugin-rsyslog = %{version}-%{release}

%description -n %{name}-logger-rsyslog
This package contains the rsyslog logger plugin for uWSGI

%package -n %{name}-logger-socket
Summary:   uWSGI - logsocket logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-loggers <= 1.9.8-1
Provides:  %{name}-loggers = %{version}-%{release}

%description -n %{name}-logger-socket
This package contains the logsocket logger plugin for uWSGI

%package -n %{name}-logger-syslog
Summary:   uWSGI - syslog logger plugin
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-plugin-syslog <= 1.9.8-1
Provides:  %{name}-plugin-syslog = %{version}-%{release}

%description -n %{name}-logger-syslog
This package contains the syslog logger plugin for uWSGI

%package -n %{name}-logger-systemd
Summary:  uWSGI - SystemD Journal logger plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-logger-systemd
This package contains the SystemD Journal logger plugin for uWSGI

%package -n %{name}-logger-zeromq
Summary:  uWSGI - ZeroMQ logger plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, zeromq

%description -n %{name}-logger-zeromq
This package contains the ZeroMQ logger plugin for uWSGI

# Plugins

%package -n %{name}-plugin-airbrake
Summary:  uWSGI - Plugin for AirBrake support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libcurl

%description -n %{name}-plugin-airbrake
This package contains the airbrake plugin for uWSGI

%package -n %{name}-plugin-cache
Summary:  uWSGI - Plugin for cache support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-cache
This package contains the cache plugin for uWSGI

%package -n %{name}-plugin-carbon
Summary:  uWSGI - Plugin for Carbon/Graphite support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-carbon
This package contains the Carbon plugin for uWSGI (to use in graphite)

%package -n %{name}-plugin-coroae
Summary:  uWSGI - Plugin for PERL Coro support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, %{name}-plugin-psgi, perl-Coro

%description -n %{name}-plugin-coroae
This package contains the coroae plugin for uWSGI

%package -n %{name}-plugin-cplusplus
Summary:  uWSGI - Plugin for C++ support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libstdc++

%description -n %{name}-plugin-cplusplus
This package contains the cplusplus plugin for uWSGI

%package -n %{name}-plugin-curl-cron
Summary:  uWSGI - Plugin for CURL Cron support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libcurl

%description -n %{name}-plugin-curl-cron
This package contains the curl_cron plugin for uWSGI

%package -n %{name}-plugin-dumbloop
Summary:  uWSGI - Plugin for Dumb Loop support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-dumbloop
This package contains the dumbloop plugin for uWSGI

%package -n %{name}-plugin-fiber
Summary:  uWSGI - Plugin for Ruby Fiber support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, %{name}-plugin-rack

%description -n %{name}-plugin-fiber
This package contains the fiber plugin for uWSGI

%package -n %{name}-plugin-gccgo
Summary:  uWSGI - Plugin for GoLang support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libgo

%description -n %{name}-plugin-gccgo
This package contains the gccgo plugin for uWSGI

%package -n %{name}-plugin-geoip
Summary:  uWSGI - Plugin for GeoIP support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, GeoIP

%description -n %{name}-plugin-geoip
This package contains the geoip plugin for uWSGI

%package -n %{name}-plugin-gevent
Summary:  uWSGI - Plugin for GEvent support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libevent

%description -n %{name}-plugin-gevent
This package contains the gevent plugin for uWSGI

%package -n %{name}-plugin-glusterfs
Summary:  uWSGI - Plugin for GlusterFS support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, glusterfs-api

%description -n %{name}-plugin-glusterfs
This package contains the glusterfs plugin for uWSGI

%package -n %{name}-plugin-greenlet
Summary:  uWSGI - Plugin for Python Greenlet support
Group:    System Environment/Daemons   
Requires: python-greenlet, %{name}-plugin-common

%description -n %{name}-plugin-greenlet
This package contains the python greenlet plugin for uWSGI

%package -n %{name}-plugin-gridfs
Summary:  uWSGI - Plugin for GridFS support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, libmongodb

%description -n %{name}-plugin-gridfs
This package contains the gridfs plugin for uWSGI

%package -n %{name}-plugin-jvm
Summary:  uWSGI - Plugin for JVM support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, java-headless, jpackage-utils

%description -n %{name}-plugin-jvm
This package contains the JVM plugin for uWSGI

%package -n %{name}-plugin-jwsgi
Summary:  uWSGI - Plugin for JWSGI support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, %{name}-plugin-jvm

%description -n %{name}-plugin-jwsgi
This package contains the jwsgi plugin for uWSGI

%package -n %{name}-plugin-lua
Summary:  uWSGI - Plugin for LUA support
Group:    System Environment/Daemons   
Requires: lua, %{name}-plugin-common

%description -n %{name}-plugin-lua
This package contains the lua plugin for uWSGI

%package -n %{name}-plugin-mongrel2
Summary:  uWSGI - Plugin for Mongrel2 support
Group:    System Environment/Daemons   
Requires: %{name}-plugin-common, zeromq

%description -n %{name}-plugin-mongrel2
This package contains the mongrel2 plugin for uWSGI

%package -n %{name}-plugin-mono
Summary:  uWSGI - Plugin for Mono / .NET support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, mono-web

%description -n %{name}-plugin-mono
This package contains the mono plugin for uWSGI

%package -n %{name}-plugin-nagios
Summary:  uWSGI - Plugin for Nagios support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-nagios
This package contains the nagios plugin for uWSGI

%package -n %{name}-plugin-pam
Summary:  uWSGI - Plugin for PAM support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, pam

%description -n %{name}-plugin-pam
This package contains the PAM plugin for uWSGI

%package -n %{name}-plugin-php
Summary:  uWSGI - Plugin for PHP support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-php
This package contains the PHP plugin for uWSGI

%package -n %{name}-plugin-psgi
Summary:  uWSGI - Plugin for PSGI support
Group:    System Environment/Daemons
Requires: perl-PSGI, %{name}-plugin-common

%description -n %{name}-plugin-psgi
This package contains the PSGI plugin for uWSGI

%package -n %{name}-plugin-pty
Summary:  uWSGI - Plugin for PTY support
Group:    System Environment/Daemons
Requires: python, %{name}-plugin-common

%description -n %{name}-plugin-pty
This package contains the pty plugin for uWSGI

%package -n %{name}-plugin-python
Summary:  uWSGI - Plugin for Python support
Group:    System Environment/Daemons
Requires: python, %{name}-plugin-common

%description -n %{name}-plugin-python
This package contains the python plugin for uWSGI

%package -n %{name}-plugin-python3
Summary:  uWSGI - Plugin for Python 3.2 support
Group:    System Environment/Daemons   
Requires: python3, %{name}-plugin-common

%description -n %{name}-plugin-python3
This package contains the Python 3.2 plugin for uWSGI

%package -n %{name}-plugin-rack
Summary:  uWSGI - Ruby rack plugin
Group:    System Environment/Daemons
Requires: rubygem-rack, %{name}-plugin-common

%description -n %{name}-plugin-rack
This package contains the rack plugin for uWSGI

%package -n %{name}-plugin-rbthreads
Summary:  uWSGI - Ruby native threads support plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, ruby

%description -n %{name}-plugin-rbthreads
This package contains the rbthreads plugin for uWSGI

%package -n %{name}-plugin-ring
Summary:  uWSGI - Clojure/Ring request handler support plugin
Group:    System Environment/Daemons
Requires: %{name}-plugin-common, %{name}-plugin-jvm, clojure

%description -n %{name}-plugin-ring
This package contains the ring plugin for uWSGI

%package -n %{name}-plugin-rpc
Summary:  uWSGI - Plugin for RPC support
Group:    System Environment/Daemons
Requires: rrdtool, %{name}-plugin-common

%description -n %{name}-plugin-rpc
This package contains the RPC plugin for uWSGI

%package -n %{name}-plugin-rrdtool
Summary:  uWSGI - Plugin for RRDTool support
Group:    System Environment/Daemons
Requires: rrdtool, %{name}-plugin-common

%description -n %{name}-plugin-rrdtool
This package contains the RRD Tool plugin for uWSGI

%package -n %{name}-plugin-ruby
Summary:  uWSGI - Plugin for Ruby support
Group:    System Environment/Daemons   
Requires: ruby, %{name}-plugin-common

%description -n %{name}-plugin-ruby
This package contains the ruby19 plugin for uWSGI

%package -n %{name}-plugin-spooler
Summary:  uWSGI - Plugin for Remote Spooling support
Group:    System Environment/Daemons   
Requires: %{name}-plugin-common

%description -n %{name}-plugin-spooler
This package contains the spooler plugin for uWSGI

%package -n %{name}-plugin-ugreen
Summary:  uWSGI - Plugin for uGreen support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-ugreen
This package contains the uGreen plugin for uWSGI

%package -n %{name}-plugin-zergpool
Summary:  uWSGI - Plugin for zergpool support
Group:    System Environment/Daemons
Requires: %{name}-plugin-common

%description -n %{name}-plugin-zergpool
This package contains the zergpool plugin for uWSGI

# Routers

%package -n %{name}-router-access
Summary:   uWSGI - Plugin for router_access router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-access
This package contains the router_access plugin for uWSGI

%package -n %{name}-router-basicauth
Summary:   uWSGI - Plugin for Basic Auth router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-basicauth
This package contains the basicauth plugin for uWSGI

%package -n %{name}-router-cache
Summary:   uWSGI - Plugin for Cache router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-cache
This package contains the cache router plugin for uWSGI

%package -n %{name}-router-expires
Summary:   uWSGI - Plugin for Expires router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-expires
This package contains the expires router plugin for uWSGI

%package -n %{name}-router-fast
Summary:   uWSGI - Plugin for FastRouter support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-plugin-fastrouter <= 2.0.6
Provides:  %{name}-plugin-fastrouter = %{version}-%{release}
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-fast
This package contains the fastrouter (proxy) plugin for uWSGI

%package -n %{name}-router-forkpty
Summary:   uWSGI - Plugin for ForkPTY router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common

%description -n %{name}-router-forkpty
This package contains the ForkPTY router plugin for uWSGI

%package -n %{name}-router-hash
Summary:   uWSGI - Plugin for Hash router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-hash
This package contains the hash router plugin for uWSGI

%package -n %{name}-router-http
Summary:   uWSGI - Plugin for HTTP router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-http
This package contains the http router plugin for uWSGI

%package -n %{name}-router-memcached
Summary:   uWSGI - Plugin for Memcached router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-memcached
This package contains the memcached router plugin for uWSGI

%package -n %{name}-router-metrics
Summary:   uWSGI - Plugin for Metrics router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common

%description -n %{name}-router-metrics
This package contains the metrics router plugin for uWSGI

%package -n %{name}-router-radius
Summary:   uWSGI - Plugin for Radius router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common

%description -n %{name}-router-radius
This package contains the metrics router plugin for uWSGI

%package -n %{name}-router-raw
Summary:   uWSGI - Plugin for Raw Router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-plugin-rawrouter <= 2.0.6
Provides:  %{name}-plugin-rawrouter = %{version}-%{release}
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-raw
This package contains the Raw router plugin for uWSGI

%package -n %{name}-router-redirect
Summary:   uWSGI - Plugin for Redirect router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-redirect
This package contains the redirect router plugin for uWSGI

%package -n %{name}-router-redis
Summary:   uWSGI - Plugin for Redis router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-redis
This package contains the redis router plugin for uWSGI

%package -n %{name}-router-rewrite
Summary:   uWSGI - Plugin for Rewrite router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-rewrite
This package contains the rewrite router plugin for uWSGI

%package -n %{name}-router-spnego
Summary:   uWSGI - Plugin for SPNEgo router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common

%description -n %{name}-router-spnego
This package contains the spnego router plugin for uWSGI

%package -n %{name}-router-ssl
Summary:   uWSGI - Plugin for SSL router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Obsoletes: %{name}-plugin-sslrouter <= 2.0.6
Provides:  %{name}-plugin-sslrouter = %{version}-%{release}
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-ssl
This package contains the SSL router plugin for uWSGI

%package -n %{name}-router-static
Summary:   uWSGI - Plugin for Static router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-static
This package contains the Static router plugin for uWSGI

%package -n %{name}-router-uwsgi
Summary:   uWSGI - Plugin for uWSGI router support
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-uwsgi
This package contains the uwsgi router plugin for uWSGI

%package -n %{name}-router-xmldir
Summary:   uWSGI - Plugin for XMLDir router rupport
Group:     System Environment/Daemons
Requires:  %{name}-plugin-common
Provides:  %{name}-routers = %{version}-%{release}

%description -n %{name}-router-xmldir
This package contains the xmldir router plugin for uWSGI

# The rest

%package -n mod_proxy_%{name}
Summary:  uWSGI - Apache2 proxy module
Group:    System Environment/Daemons
Requires: %{name}, httpd

%description -n mod_proxy_%{name}
Fully Apache API compliant proxy module


%prep
%setup -q
cp -p %{SOURCE1} buildconf/
cp -p %{SOURCE2} %{name}.service
cp -p %{SOURCE3} %{name}.ini
cp -p %{SOURCE4} uwsgi-docs.tar.gz
cp -p %{SOURCE5} README.Fedora
echo "plugin_dir = %{_libdir}/%{name}" >> buildconf/$(basename %{SOURCE1})
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CFLAGS="%{optflags} -Wno-unused-but-set-variable" python uwsgiconfig.py --build fedora.ini
CFLAGS="%{optflags} -Wno-unused-but-set-variable" python3 uwsgiconfig.py --plugin plugins/python fedora python3
%{_httpd_apxs} -Wc,-Wall -Wl -c apache2/mod_proxy_uwsgi.c

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}/run/%{name}
mkdir -p %{buildroot}%{_httpd_moddir}
mkdir -p %{buildroot}/usr/lib/mono/gac/
mkdir docs
tar -C docs/ --strip-components=1 -xvzf uwsgi-docs.tar.gz
cp docs/Changelog-%{majornumber}.%{minornumber}.%{releasenumber}.rst CHANGELOG
echo "%{commit}, i.e. this:" >> README.Fedora
echo "https://github.com/unbit/%{docrepo}/tree/%{commit}" >> README.Fedora
%{__install} -p -m 0755 %{name} %{buildroot}%{_sbindir}
%{__install} -p -m 0644 *.h %{buildroot}%{_includedir}/%{name}
%{__install} -p -m 0755 *_plugin.so %{buildroot}%{_libdir}/%{name}
%{__install} -p -m 0644 plugins/jvm/%{name}.jar %{buildroot}%{_javadir}
gacutil -i plugins/mono/uwsgi.dll -f -package %{name} -root %{buildroot}/usr/lib
%{__install} -p -m 0644 %{name}.ini %{buildroot}%{_sysconfdir}/%{name}.ini
%{__install} -p -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -m 0755 apache2/.libs/mod_proxy_%{name}.so %{buildroot}%{_httpd_moddir}/mod_proxy_%{name}.so


%pre
getent group uwsgi >/dev/null || groupadd -r uwsgi
getent passwd uwsgi >/dev/null || \
    useradd -r -g uwsgi -d /run/uwsgi -s /sbin/nologin \
    -c "uWSGI daemon user" uwsgi
exit 0

%post
%if 0%{?systemd_post:1}
    %systemd_post uwsgi.service
%else
    if [ $1 -eq 1 ] ; then 
        # Initial installation 
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    fi
%endif

%preun
%if 0%{?systemd_preun:1}
    %systemd_preun uwsgi.service
%else
    if [ $1 -eq 0 ] ; then
        # Package removal, not upgrade
        /bin/systemctl --no-reload disable uwsgi.service > /dev/null 2>&1 || :
        /bin/systemctl stop uwsgi.service > /dev/null 2>&1 || :
    fi
%endif

%postun
%if 0%{?systemd_postun:1}
    %systemd_postun uwsgi.service
%else
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    if [ $1 -ge 1 ] ; then
        # Package upgrade, not uninstall
        /bin/systemctl try-restart uwsgi.service >/dev/null 2>&1 || :
    fi
%endif


%files 
%{_sbindir}/%{name}
%{_sysconfdir}/%{name}.ini
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}.d
%dir /run/%{name}
%doc LICENSE README README.Fedora CHANGELOG

%files -n %{name}-devel
%{_includedir}/%{name}

%files -n %{name}-docs
%doc docs

%files -n %{name}-plugin-common
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/http_plugin.so
%{_libdir}/%{name}/cgi_plugin.so

# Alarms

%files -n %{name}-alarm-curl
%{_libdir}/%{name}/alarm_curl_plugin.so

%files -n %{name}-alarm-xmpp
%{_libdir}/%{name}/alarm_xmpp_plugin.so

# Loggers

%files -n %{name}-log-encoder-msgpack
%{_libdir}/%{name}/msgpack_plugin.so

%files -n %{name}-logger-crypto
%{_libdir}/%{name}/logcrypto_plugin.so

%files -n %{name}-logger-file
%{_libdir}/%{name}/logfile_plugin.so

%files -n %{name}-logger-graylog2
%{_libdir}/%{name}/graylog2_plugin.so

%files -n %{name}-logger-mongodb
%{_libdir}/%{name}/mongodblog_plugin.so

%files -n %{name}-logger-pipe
%{_libdir}/%{name}/logpipe_plugin.so

%files -n %{name}-logger-redis
%{_libdir}/%{name}/redislog_plugin.so

%files -n %{name}-logger-rsyslog
%{_libdir}/%{name}/rsyslog_plugin.so

%files -n %{name}-logger-socket
%{_libdir}/%{name}/logsocket_plugin.so

%files -n %{name}-logger-syslog
%{_libdir}/%{name}/syslog_plugin.so

%files -n %{name}-logger-systemd
%{_libdir}/%{name}/systemd_logger_plugin.so

%files -n %{name}-logger-zeromq
%{_libdir}/%{name}/logzmq_plugin.so

# Plugins

%files -n %{name}-plugin-airbrake
%{_libdir}/%{name}/airbrake_plugin.so

%files -n %{name}-plugin-cache
%{_libdir}/%{name}/cache_plugin.so

%files -n %{name}-plugin-carbon
%{_libdir}/%{name}/carbon_plugin.so

%files -n %{name}-plugin-coroae
%{_libdir}/%{name}/coroae_plugin.so

%files -n %{name}-plugin-cplusplus
%{_libdir}/%{name}/cplusplus_plugin.so

%files -n %{name}-plugin-curl-cron
%{_libdir}/%{name}/curl_cron_plugin.so

%files -n %{name}-plugin-dumbloop
%{_libdir}/%{name}/dumbloop_plugin.so

%files -n %{name}-plugin-fiber
%{_libdir}/%{name}/fiber_plugin.so

%files -n %{name}-plugin-gccgo
%{_libdir}/%{name}/gccgo_plugin.so

%files -n %{name}-plugin-geoip
%{_libdir}/%{name}/geoip_plugin.so

%files -n %{name}-plugin-gevent
%{_libdir}/%{name}/gevent_plugin.so

%files -n %{name}-plugin-glusterfs
%{_libdir}/%{name}/glusterfs_plugin.so

%files -n %{name}-plugin-greenlet
%{_libdir}/%{name}/greenlet_plugin.so

%files -n %{name}-plugin-gridfs
%{_libdir}/%{name}/gridfs_plugin.so

%files -n %{name}-plugin-jvm
%{_libdir}/%{name}/jvm_plugin.so
%{_javadir}/uwsgi.jar

%files -n %{name}-plugin-jwsgi
%{_libdir}/%{name}/jwsgi_plugin.so

%files -n %{name}-plugin-lua
%{_libdir}/%{name}/lua_plugin.so

%files -n %{name}-plugin-mongrel2
%{_libdir}/%{name}/mongrel2_plugin.so

%files -n %{name}-plugin-mono
%dir /usr/lib/mono/%{name}/
%dir /usr/lib/mono/gac/%{name}/
%{_libdir}/%{name}/mono_plugin.so
/usr/lib/mono/%{name}/*.dll
/usr/lib/mono/gac/%{name}/*/*.dll

%files -n %{name}-plugin-nagios
%{_libdir}/%{name}/nagios_plugin.so

%files -n %{name}-plugin-pam
%{_libdir}/%{name}/pam_plugin.so

%files -n %{name}-plugin-php
%{_libdir}/%{name}/php_plugin.so

%files -n %{name}-plugin-psgi
%{_libdir}/%{name}/psgi_plugin.so

%files -n %{name}-plugin-pty
%{_libdir}/%{name}/pty_plugin.so

%files -n %{name}-plugin-python
%{_libdir}/%{name}/python_plugin.so

%files -n %{name}-plugin-python3
%{_libdir}/%{name}/python3_plugin.so

%files -n %{name}-plugin-rack
%{_libdir}/%{name}/rack_plugin.so

%files -n %{name}-plugin-rbthreads
%{_libdir}/%{name}/rbthreads_plugin.so

%files -n %{name}-plugin-ring
%{_libdir}/%{name}/ring_plugin.so

%files -n %{name}-plugin-rrdtool
%{_libdir}/%{name}/rrdtool_plugin.so

%files -n %{name}-plugin-rpc
%{_libdir}/%{name}/rpc_plugin.so

%files -n %{name}-plugin-ruby
%{_libdir}/%{name}/ruby19_plugin.so

%files -n %{name}-plugin-spooler
%{_libdir}/%{name}/spooler_plugin.so

%files -n %{name}-plugin-ugreen
%{_libdir}/%{name}/ugreen_plugin.so

%files -n %{name}-plugin-zergpool
%{_libdir}/%{name}/zergpool_plugin.so

# Routers

%files -n %{name}-router-access
%{_libdir}/%{name}/router_access_plugin.so

%files -n %{name}-router-basicauth
%{_libdir}/%{name}/router_basicauth_plugin.so

%files -n %{name}-router-cache
%{_libdir}/%{name}/router_cache_plugin.so

%files -n %{name}-router-expires
%{_libdir}/%{name}/router_expires_plugin.so

%files -n %{name}-router-fast
%{_libdir}/%{name}/fastrouter_plugin.so

%files -n %{name}-router-forkpty
%{_libdir}/%{name}/forkptyrouter_plugin.so

%files -n %{name}-router-hash
%{_libdir}/%{name}/router_hash_plugin.so

%files -n %{name}-router-http
%{_libdir}/%{name}/router_http_plugin.so

%files -n %{name}-router-memcached
%{_libdir}/%{name}/router_memcached_plugin.so

%files -n %{name}-router-metrics
%{_libdir}/%{name}/router_metrics_plugin.so

%files -n %{name}-router-radius
%{_libdir}/%{name}/router_radius_plugin.so

%files -n %{name}-router-raw
%{_libdir}/%{name}/rawrouter_plugin.so

%files -n %{name}-router-redirect
%{_libdir}/%{name}/router_redirect_plugin.so

%files -n %{name}-router-redis
%{_libdir}/%{name}/router_redis_plugin.so

%files -n %{name}-router-rewrite
%{_libdir}/%{name}/router_rewrite_plugin.so

%files -n %{name}-router-spnego
%{_libdir}/%{name}/router_spnego_plugin.so

%files -n %{name}-router-ssl
%{_libdir}/%{name}/sslrouter_plugin.so

%files -n %{name}-router-static
%{_libdir}/%{name}/router_static_plugin.so

%files -n %{name}-router-uwsgi
%{_libdir}/%{name}/router_uwsgi_plugin.so

%files -n %{name}-router-xmldir
%{_libdir}/%{name}/router_xmldir_plugin.so

# The rest

%files -n mod_proxy_%{name}
%{_httpd_moddir}/mod_proxy_%{name}.so


%changelog
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.9.19-5
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.9.19-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 1.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Nov 12 2013 Jorge A Gallegos <kad@blegh.net> - 1.9.19-1
- Updating to latest stable, uploading new sources (Jorge Gallegos)
- Forgot to delete the jvm arm patch file (Jorge Gallegos)

* Sun Oct 20 2013 Jorge A Gallegos <kad@blegh.net> - 1.9.18.2-1
- The changelog entry must match major + minor (Jorge Gallegos)
- Adding more ignore entries (Jorge Gallegos)
- The jvm arm patch has been merged upstream (Jorge Gallegos)
- Updated license to 'GPLv2 with exceptions' (Jorge Gallegos)
- Ugh messed up the doc sha (Jorge Gallegos)
- Adding new sources, bumping up spec to 1.9.18.2 (Jorge Gallegos)

* Sat Oct 19 2013 Jorge A Gallegos <kad@fedoraproject.org> - 1.9.18.2-0
- Breaking up full version in 3 parts (Jorge Gallegos)
- Update to latest stable 1.9.18.2 (Jorge Gallegos)
- Forgot to disable debug mode (Jorge Gallegos)

* Wed Oct 09 2013 Jorge A Gallegos <kad@blegh.net> - 1.9.17-2
- Uploaded new sources per spec rework (Jorge Gallegos)
- Adding more router plugins (Jorge Gallegos)
- Adding mod_proxy_uwsgi apache module (Jorge Gallegos)
- Complying with the guidelines for source urls (Jorge Gallegos)
- The settings in the service file were right before (Jorge Gallegos)
- Enabling stats log socket, and capabilities (Jorge Gallegos)

* Thu Oct 03 2013 Jorge A Gallegos <kad@blegh.net> - 1.9.17-1
- Copying the version changelog to top-level doc
- Compile with POSIX capabilities
- Embed the loggers into the binary itself, no need for an extra package
- Patching jvm plugin to support arm

* Wed Oct 02 2013 Jorge A Gallegos <kad@fedoraproject.org> - 1.9.17-0
- Rebuilt for version 1.9.17
- Pulling in new documentation from https://github.com/unbit/uwsgi-docs

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.8-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Jorge A Gallegos <kad@blegh.net> - 1.9.8-0
- Rebuilt with latest stable version from upstream

* Thu Apr 11 2013 Jorge A Gallegos <kad@blegh.net> - 1.9.5-0
- Rebuilt with latest stable version from upstream
- Added Erlang, PAM and JVM plugins
- Added router-related plugins
- Added logger plugins

* Tue Apr 02 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.6-10
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sat Mar 23 2013 Remi Collet <rcollet@redhat.com> - 1.2.6-9
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Jorge A Gallegos <kad@blegh.net> - 1.2.6-7
- Tyrant mode shouldn't be used here, tyrant mode is root-only

* Thu Dec 27 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-6
- Systemd now supports an exit status directive, fixing bugz 873382

* Fri Nov  9 2012 Remi Collet <rcollet@redhat.com> - 1.2.6-5
- rebuild against new php embedded library soname (5.4)

* Thu Oct 18 2012 Remi Collet <remi@fedoraproject.org> - 1.2.6-4
- rebuild for new PHP 5.4.8

* Wed Sep 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-3
- Dropped requirement on PHP for the PHP plugin

* Sat Sep 15 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-2
- Rebuilt with new systemd macros

* Sun Sep 09 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.6-1
- Updated to latest stable from upstream

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.2.4-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.4-1
- Updated to latest stable from upstream

* Tue Jun 26 2012 Jorge A Gallegos <kad@blegh.net> - 1.2.3-1
- Updated to latest stable upstream
- Building the pytho3 plugin is a bit trickier now, but still possible
- Added PHP plugin
- Added Carbon plugin
- Added RRDTool plugin
- Added rsyslog plugin
- Added syslog plugin

* Sun Feb 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.4-1
- Addressing issues from package review feedback
- s/python-devel/python2-devel
- Make the libdir subdir owned by -plugins-common
- Upgraded to latest stable upstream version

* Mon Feb 06 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.2.1-2
- Fixing 'unstripped-binary-or-object'

* Thu Jan 19 2012 Jorge A Gallegos <kad@blegh.net> - 1.0.2.1-1
- New upstream version

* Thu Dec 08 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.3-1
- New upstream version

* Sun Oct 09 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.2-2
- Don't download the wiki page at build time

* Sun Oct 09 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.9.2-1
- Updated to latest stable version
- Correctly linking plugin_dir
- Patches 1 and 2 were addressed upstream

* Sun Aug 21 2011 Jorge A Gallegos <kad@blegh.net> - 0.9.8.3-3
- Got rid of BuildRoot
- Got rid of defattr()

* Sun Aug 14 2011 Jorge Gallegos <kad@blegh.net> - 0.9.8.3-2
- Added uwsgi_fix_rpath.patch
- Backported json_loads patch to work with jansson 1.x and 2.x
- Deleted clean steps since they are not needed in fedora

* Sun Jul 24 2011 Jorge Gallegos <kad@blegh.net> - 0.9.8.3-1
- rebuilt
- Upgraded to latest stable version 0.9.8.3
- Split packages

* Sun Jul 17 2011 Jorge Gallegos <kad@blegh.net> - 0.9.6.8-2
- Heavily modified based on Oskari's work

* Mon Feb 28 2011 Oskari Saarenmaa <os@taisia.fi> - 0.9.6.8-1
- Initial.
