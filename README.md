# kip-system

КИП система для курсового проекта СамГТУ

## Запуск приложения без конфигурирования

```bash
cd backend
cp .env.docker .env
cd ..
docker-compose up -d --build
```

## Преднастройка окружения

```bash
cd backend 
cp .env.example .env
nano .env
```

## Документация

[Даталогическая модель](https://raw.githubusercontent.com/Niatomi/kip-system/main/docs/db/db_diagram.xml)

[Figma](https://www.figma.com/file/OFHGG9Xd23Ej4REh5Wds12/kip-system?type=design&node-id=10%3A107&t=sh6PDZga7Dl0R0HI-1)