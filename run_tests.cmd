docker build -t "lca:python" .
docker run -it --rm --name "lca-python" lca:python ./test.sh