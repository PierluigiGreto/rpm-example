# Example to generate rmp packages
## Generate src
```
rpmbuild -bs ./my-super-script.spec --define "_sourcedir $PWD"
```
## Check in the building works
```
mock --dnf --resultdir=~/rpmbuild/RPMS/ --rebuild /home/vagrant/rpmbuild/SRPMS/my-super-script-0.1-0.fc26.src.rpm
```

## Upload the src in copr
https://copr.fedorainfracloud.org/coprs/pierluigi/test/
