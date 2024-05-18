kubectl create secret docker-registry regcred --docker-server=container-registry.oracle.com --docker-username=ERFEDE@YOPMAIL.COM --docker-password=Bellapete!1 --docker-email=ERFEDE@YOPMAIL.COM -n db

kubectl create secret docker-registry regcred --docker-server=container-registry.oracle.com --docker-username=ERFEDE@YOPMAIL.COM --docker-password=Bellapete!1 --docker-email=ERFEDE@YOPMAIL.COM -n db


helm install db19c -f values.yaml oracle-db-1.0.0.tgz -n db
helm uninstall db19c -n db


{"auths":{"container-registry.oracle.com":{"username":"erfede@yopmail.com","password":"Bellapete!1","email":"erfede@yopmail.com","auth":"ZXJmZWRlQHlvcG1haWwuY29tOkJlbGxhcGV0ZSEx"}}}