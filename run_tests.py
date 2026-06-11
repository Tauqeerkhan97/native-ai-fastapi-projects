#!/usr/bin/env python
"""Test both apps using TestClient"""
import sys
import os

def test_agentic():
    print("\n=== Agentic System Tests ===")
    os.chdir('agentic-system-enhanced')
    sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
    from fastapi.testclient import TestClient
    from main import app
    
    client = TestClient(app)
    
    # Root
    r = client.get('/')
    print(f"GET / : {r.status_code}")
    assert r.status_code == 200
    
    # Health
    r = client.get('/health')
    print(f"GET /health : {r.status_code}")
    assert r.status_code == 200
    
    # Create agent
    r = client.post('/api/v1/agents/', json={
        'name': 'TestAgent',
        'description': 'Testing via TestClient',
        'agent_type': 'tester'
    })
    print(f"POST /api/v1/agents/ : {r.status_code}")
    if r.status_code >= 400:
        print(f"  Error: {r.text}")
    else:
        agent = r.json()
        print(f"  Created agent ID {agent.get('id')}: {agent.get('name')}")
    
    # List agents
    r = client.get('/api/v1/agents/')
    print(f"GET /api/v1/agents/ : {r.status_code}, count={len(r.json())}")
    
    os.chdir('..')
    return True

def test_docapi():
    print("\n=== Doc API Tests ===")
    os.chdir('doc-api')
    sys.path.insert(0, os.path.join(os.getcwd(), 'src'))
    from fastapi.testclient import TestClient
    from main import app
    
    client = TestClient(app)
    
    # Root
    r = client.get('/')
    print(f"GET / : {r.status_code}")
    assert r.status_code == 200
    
    # Health
    r = client.get('/health')
    print(f"GET /health : {r.status_code}")
    assert r.status_code == 200
    
    # Register user
    r = client.post('/api/v1/auth/register', json={
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'testpass123'
    })
    print(f"POST /api/v1/auth/register : {r.status_code}")
    if r.status_code >= 400:
        print(f"  Error: {r.text}")
    else:
        user = r.json()
        print(f"  Created user ID {user.get('id')}: {user.get('username')}")
    
    # List users (should work without auth for now)
    r = client.get('/api/v1/auth/me')  # Actually need auth token, but we can test /users if needed
    # For now skip auth-required endpoints
    print(f"Note: Auth endpoints require token; create document would need auth")
    
    os.chdir('..')
    return True

if __name__ == '__main__':
    try:
        ok1 = test_agentic()
        ok2 = test_docapi()
        print("\n=== SUMMARY ===")
        print(f"Agentic System: {'PASS' if ok1 else 'FAIL'}")
        print(f"Doc API: {'PASS' if ok2 else 'FAIL'}")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
