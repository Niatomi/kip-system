run: 
	cd backend
	cp .env.docker .env
	cd ..
	docker-compose up -d --build