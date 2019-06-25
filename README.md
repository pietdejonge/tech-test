## 1. System Preparation and Info 
First, I created an EC2 instance on AWS. Key software versions:

`hostname`  
ip-10-0-0-240.eu-west-1.compute.internal


`uname -a`  
Linux ip-10-0-0-240.eu-west-1.compute.internal 4.14.123-111.109.amzn2.x86_64 #1 SMP Mon Jun 10 19:37:57 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux


`docker version`
```
Client:
 Version:           18.06.1-ce
 API version:       1.38
 Go version:        go1.10.3
 Git commit:        e68fc7a215d7133c34aa18e3b72b4a21fd0c6136
 Built:             Mon Mar  4 21:25:41 2019
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          18.06.1-ce
  API version:      1.38 (minimum version 1.12)
  Go version:       go1.10.3
  Git commit:       e68fc7a/18.06.1-ce
  Built:            Mon Mar  4 21:27:07 2019
  OS/Arch:          linux/amd64
  Experimental:     false
```
`oc version`

oc v3.11.0+0cbc58b
kubernetes v1.11.0+d4cacc0
features: Basic-Auth GSSAPI Kerberos SPNEGO

Server https://127.0.0.1:8443
kubernetes v1.11.0+d4cacc0


## 2. Creating repository 
https://github.com/sushanco/temp-repo

## 3. Added README.md to keep log of activities and config files
### Downloading and setup oc client 

[ec2-user@ip-10-0-0-240 ~]$ wget -q https://github.com/openshift/origin/releases/download/v3.11.0/openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz


[ec2-user@ip-10-0-0-240 ~]$ tar -xvf openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit.tar.gz

[ec2-user@ip-10-0-0-240 ]$ sudo mv openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit/oc /usr/bin/

Install docker 
[ec2-user@ip-10-0-0-240 ]$ sudo yum install docker -y

Modify docker deamon config file 
[ec2-user@ip-10-0-0-240 ]$ sudo vim /etc/sysconfig/docker

Added insecure-registry and add-registry
OPTIONS='--insecure-registry 172.0.0.0/16'


For security reasons I decided to private host as public hostname of the cluseter and modify local host file to access the url.
Modified 

Cluster Up:
oc cluster up --public-hostname=ip-10-0-0-240.eu-west-1.compute.internal

Login as admin to see cluster status:
[root@ip-10-0-0-240 ~]# oc login -u system:admin
```
Logged into "https://127.0.0.1:8443" as "system:admin" using existing credentials.

You have access to the following projects and can switch between them with 'oc project <projectname>':

    default
    kube-dns
    kube-proxy
    kube-public
    kube-system
    myproject
    openshift
    openshift-apiserver
    openshift-controller-manager
    openshift-core-operators
    openshift-infra
    openshift-node
    openshift-service-cert-signer
    openshift-web-console

Using project "myproject".
```

[root@ip-10-0-0-240 ~]# oc get pods --all-namespaces
```
NAMESPACE                       NAME                                                      READY     STATUS      RESTARTS   AGE
default                         docker-registry-1-fpd9f                                   1/1       Running     0          17m
default                         persistent-volume-setup-87755                             0/1       Completed   0          17m
default                         router-1-wz4c4                                            1/1       Running     0          17m
kube-dns                        kube-dns-tjc2g                                            1/1       Running     0          18m
kube-proxy                      kube-proxy-vtjzl                                          1/1       Running     0          18m
kube-system                     kube-controller-manager-localhost                         1/1       Running     0          18m
kube-system                     kube-scheduler-localhost                                  1/1       Running     0          18m
kube-system                     master-api-localhost                                      1/1       Running     0          18m
kube-system                     master-etcd-localhost                                     1/1       Running     0          18m
openshift-apiserver             openshift-apiserver-vjg74                                 1/1       Running     0          18m
openshift-controller-manager    openshift-controller-manager-k9h6w                        1/1       Running     0          17m
openshift-core-operators        openshift-service-cert-signer-operator-6d477f986b-hfp24   1/1       Running     0          18m
openshift-core-operators        openshift-web-console-operator-664b974ff5-vmjbv           1/1       Running     0          17m
openshift-service-cert-signer   apiservice-cabundle-injector-8ffbbb6dc-4ch96              1/1       Running     0          18m
openshift-service-cert-signer   service-serving-cert-signer-668c45d5f-jc4rs               1/1       Running     0          18m
openshift-web-console           webconsole-657cbc5c6b-jtlk8                               1/1       Running     0          17m
```


[root@ip-10-0-0-240 python-app]# curl python-web-app-svc-myproject.127.0.0.1.nip.io
Hello world! Howdy?

