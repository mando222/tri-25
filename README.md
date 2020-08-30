# tri-25

Requirements:

go 1.13+
```
cd ~/Downloads
wget -c https://storage.googleapis.com/golang/go1.15.linux-amd64.tar.gz
sudo tar -C /usr/local -xvzf go1.15.linux-amd64.tar.gz
mkdir -p ~/go_projects/{bin,src,pkg}
cd ~/go_projects

```

in your ~/.zshrc or ~/.bashrc or ~/.bash_profile set the following
```
export PATH=$PATH:/usr/local/go/bin
export GOPATH="$HOME/go_projects"
export GOBIN="$GOPATH/bin"
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin
```
