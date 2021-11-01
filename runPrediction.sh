
docker run -v `pwd`/src:/src -v `pwd`/data:/data wlo-langdetect-py python3 /src/langdetector.py  "$1"