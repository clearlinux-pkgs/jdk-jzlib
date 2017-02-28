Name     : jdk-jzlib
Version  : 1.1.3
Release  : 1
URL      : https://github.com/ymnk/jzlib/archive/1.1.3.tar.gz
Source0  : https://github.com/ymnk/jzlib/archive/1.1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-maven-shared-incremental
BuildRequires : apache-maven2
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-plexus-io
BuildRequires : jdk-commons-compress
BuildRequires : jdk-snappy
BuildRequires : jdk-xz
BuildRequires : jdk-xmlunit
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-velocity
BuildRequires : jdk-commons-collections
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-doxia
BuildRequires : jdk-log4j
BuildRequires : jdk-xbean
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-surefire
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch1: jzlib-javadoc-fixes.patch

%description
JZlib
zlib in pure Java(TM)
by ymnk@jcraft.com, JCraft,Inc.
http://www.jcraft.com/jzlib/

%prep
%setup -q -n jzlib-1.1.3
%patch1

python3 /usr/share/java-utils/mvn_file.py : jzlib

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n jzlib -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/jzlib.jar
/usr/share/maven-metadata/jzlib.xml
/usr/share/maven-poms/jzlib.pom
