import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

@pytest.mark.asyncio
async def test_crud_operations():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # CREATE
        create_response = await ac.post("/todos/", json={
            "title": "Test Task",
            "description": "testing create"
        })
        assert create_response.status_code == status.HTTP_200_OK
        todo = create_response.json()
        todo_id = todo["_id"]

        # READ ALL
        get_all_response = await ac.get("/todos/")
        assert get_all_response.status_code == status.HTTP_200_OK
        assert any(t["_id"] == todo_id for t in get_all_response.json())

        # READ BY ID
        get_one_response = await ac.get(f"/todos/{todo_id}")
        assert get_one_response.status_code == status.HTTP_200_OK
        assert get_one_response.json()["title"] == "Test Task"

        # UPDATE
        update_response = await ac.put(f"/todos/{todo_id}", json={
            "title": "Updated Todo",
            "description": "Updated description",
            "completed": True
        })
        assert update_response.status_code == status.HTTP_200_OK
        assert update_response.json()["title"] == "Updated Todo"

        # DELETE
        delete_response = await ac.delete(f"/todos/{todo_id}")
        assert delete_response.status_code == status.HTTP_200_OK

        # VERIFY DELETION
        check_deleted = await ac.get(f"/todos/{todo_id}")
        assert check_deleted.status_code == status.HTTP_404_NOT_FOUND











"""import pytest
from fastapi.testclient import TestClient
from fastapi import status
from httpx import AsyncClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_crud_operations():
    async with AsyncClient(app=app, base_url="http://test") as ac:
            # app запускается отдельно, или через отдельный фикстур
            create_response = await ac.post("http://127.0.0.1:8000/todos/", json={
                "title": "Test Task",
                "description": "testing create"
            })
            assert create_response.status_code == status.HTTP_200_OK
            todo = create_response.json()
            todo_id = todo["_id"]

            # Read all
            get_all_response = await ac.get("/todos/")
            assert get_all_response.status_code == status.HTTP_200_OK
            assert any(t["_id"] == todo_id for t in get_all_response.json())

            # Read by ID
            get_one_response = await ac.get(f"/todos/{todo_id}")
            assert get_one_response.status_code == status.HTTP_200_OK
            assert get_one_response.json()["title"] == "Test Todo"

            # Update
            update_response = await ac.put(f"/todos/{todo_id}", json={
                "title": "Updated Todo",
                "description": "Updated description",
                "completed": True
            })
            assert update_response.status_code == status.HTTP_200_OK
            assert update_response.json()["title"] == "Updated Todo"

            # Delete
            delete_response = await ac.delete(f"/todos/{todo_id}")
            assert delete_response.status_code == status.HTTP_200_OK

            # Check deletion
            check_deleted = await ac.get(f"/todos/{todo_id}")
            assert check_deleted.status_code == status.HTTP_404_NOT_FOUND"""



"""async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create
        create_response = await ac.post("/todos/", json={
            "title": "Test Todo",
            "description": "For testing"
        })
        assert create_response.status_code == status.HTTP_200_OK
        todo = create_response.json()"""



"""@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(base_url="http://testserver") as ac:
        # app запускается отдельно, или через отдельный фикстур
        response = await ac.post("http://127.0.0.1:8000/todos/", json={
            "title": "Test Task",
            "description": "testing create"
        })
    assert response.status_code == status.HTTP_200_OK"""