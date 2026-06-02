# Docker Quick Start Guide

This guide covers the basic commands needed to manage the Cuantum Computing Simulator using Docker.

## Prerequisite
Make sure you are in the root directory of the project (where the `docker-compose.yml` file is located) before running any of these commands.

## Start the Containers
To start both the frontend and backend in the background:
```bash
docker compose up -d
```
* **Frontend** will be available at: http://localhost:4321
* **Backend API** will be available at: http://localhost:8000/docs

## Stop the Containers
To stop and remove the running containers safely:
```bash
docker compose down
```
*(Note: Your data in `backend/data` is safely preserved on your local machine)*

## Update after Code Changes
If you make changes to your Python files under `backend/` or your Astro files under `frontend/`, you need to tell Docker to rebuild the images so those changes take effect:
```bash
docker compose up -d --build
```
The `--build` flag forces Docker to re-read your files and recreate the frontend and backend images.

## Useful Extra Commands

### View Logs
If you want to see what is happening inside the containers (useful for debugging errors):
```bash
docker compose logs -f
```
Press `Ctrl+C` to stop watching the logs.

### Check Status
To see if your containers are running:
```bash
docker ps
```