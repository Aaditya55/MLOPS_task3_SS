FROM centos:latest

RUN yum install python36 -y

RUN python3 -m pip install --upgrade pip

RUN yum install -y epel-release

RUN yum groupinstall "developement tools " -y 

RUN yum install -y python36-devel

RUN pip3 install keras

RUN pip3 numpy

RUN pip3 opencv-python

RUN pip3 --upgrade tensorflow

RUN pip3 pandas 

RUN pip3 matplotlib

RUN pip3 pillow