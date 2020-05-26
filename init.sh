#!/usr/bin/env bash

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#basepath=$(cd `dirname $0`;pwd)

cd $(dirname $BASH_SOURCE)
basepath=`echo $(pwd)`
init() {

	system=`awk -F= '/^NAME/{print $2}' /etc/os-release`
	echo ${system}
	case "${system}" in
        "\"CentOS Linux\"")
                echo "CentOS System"
                sudo yum -y install gcc gcc-c++ make autoconfig openssl-devel supervisor gmp-devel mpfr-devel libmpc-devel libaio numactl autoconf automake libtool libffi-dev
                ;;
        \""Ubuntu\"")
                echo "Ubuntu System"
#		sudo apt-get install gcc g++ make  openssl supervisor libgmp-dev  libmpfr-dev libmpc-dev libaio1 libaio-dev numactl autoconf automake libtool libffi-dev libssl1.0.0 libssl-dev  liblz4-1 liblz4-dev liblz4-1-dbg liblz4-tool  zlib1g zlib1g-dbg zlib1g-dev
		cd /usr/lib/x86_64-linux-gnu
		if [ ! -f "libssl.so.10" ];then
			   sudo ln -s libssl.so.1.0.0 libssl.so.10
			      sudo ln -s libcrypto.so.1.0.0 libcrypto.so.10
		      fi
                ;;
        *)
                echo "Not support this system."

	esac

	cd ${basepath}
	export PYTHONPATH=${basepath}:${basepath}/eggroll/python
	export PATH=${basepath}/miniconda3-fate-1.1/bin:$PATH
	echo ${PATH}
	echo "#!/bin/sh
export PATH=${basepath}/miniconda3-fate-1.1/bin:\$PATH" > ${basepath}/miniconda3-fate-1.1/bin/activate
	sed -i.bak "s#!.*python#!${basepath}/miniconda3-fate-1.1/bin/python#g" ${basepath}/miniconda3-fate-1.1/bin/conda
	sed -i.bak "s#!.*python#!${basepath}/miniconda3-fate-1.1/bin/python#g" ${basepath}/miniconda3-fate-1.1/bin/conda-env

	sed -i.bak "s#fateboard.datasource.jdbc-url=.*#fateboard.datasource.jdbc-url=jdbc:sqlite:$basepath/fate_flow/fate_flow_sqlite.db#g" ${basepath}/fateboard/conf/application.properties
	sed -i.bak "s#venv=.*#venv=${basepath}/miniconda3-fate-1.1#g" ${basepath}/fate_flow/service.sh
	sed -i.bak "s#PYTHONPATH=.*#PYTHONPATH=${basepath}#g" ${basepath}/fate_flow/service.sh

	sed -i.bak "s#\#!.*#\#!${basepath}/miniconda3-fate-1.1/bin/python#g" ${basepath}/miniconda3-fate-1.1/bin/coverage

	cd  $basepath/fate_flow
	bash  service.sh restart
	cd  $basepath/fateboard
	bash  service.sh restart
	cd $basepath  
}

action() {
        cd  $basepath/fate_flow
        bash  service.sh $1
        cd  $basepath/fateboard
        bash  service.sh $1
        cd $basepath
}

case "$1" in
    start)
        action $@
        ;;

    stop)
        action $@
        ;;
    status)
        action $@
        ;;

    init)
	init
        ;;
    *)
        echo "usage: $0 {start|stop|status|init}"
        exit -1
esac


