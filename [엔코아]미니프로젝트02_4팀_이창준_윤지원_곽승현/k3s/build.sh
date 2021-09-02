#!/bin/bash
sudo apt update && sudo upgrade
curl -sfL https://get.k3s.io | sh -
sudo systemctl status k3s
sudo kubectl get node
sudo kubectl get pod --namespace=kube-system
