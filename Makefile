shell:
	rshell -p /dev/ttyUSB0
	
start:
	docker run -d -p 8080:80 binwiederhier/ntfy serve
