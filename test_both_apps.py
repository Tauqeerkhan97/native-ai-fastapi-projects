#!/usr/bin/env python
"""Test both applications"""
import sys
import os

def test_agentic_system():
    print("\n=== Testing Agentic System Enhanced ===")
    os.chdir('agentic-system-enhanced')
    sys.path.insert(0, 'src')
    
    try:
        from models import Agent, Task
        from services.agent_service import AgentService
        print("✓ Imports successful")
    except Exception as e:
        print(f"✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    try:
        from database import get_db
        db = next(get_db())
        
        agents = AgentService.get_agents(db, limit=5)
        print(f"✓ Found {len(agents)} agents in database")
        
        if agents:
            print(f"  Sample agent: {agents[0].name} (type: {agents[0].agent_type})")
        
        from services.task_service import TaskService
        from schemas import TaskCreate
        task = TaskService.create_task(db, TaskCreate(
            title="Test Task",
            description="Testing task creation",
            priority="medium"
        ))
        print(f"✓ Created task: {task.title} (ID: {task.id})")
        
        if agents:
            AgentService.assign_task_to_agent(db, task.id, agents[0].id)
            print(f"✓ Assigned task to agent: {agents[0].name}")
        
        db.close()
    except Exception as e:
        print(f"✗ Database operations failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def test_doc_api():
    print("\n=== Testing Internal Documentation API ===")
    os.chdir('../doc-api')
    sys.path.insert(0, 'src')
    
    try:
        from models import User, Document
        from services.user_service import UserService
        print("✓ Imports successful")
    except Exception as e:
        print(f"✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    try:
        from database import get_db
        db = next(get_db())
        
        users = UserService.get_users(db, limit=5)
        print(f"✓ Found {len(users)} users in database")
        
        if users:
            print(f"  Sample user: {users[0].username} (email: {users[0].email})")
        
        from services.auth_service import AuthService
        hashed = AuthService.get_password_hash("test123")
        print(f"✓ Password hashing works")
        
        if users:
            from services.document_service import DocumentService
            from schemas import DocumentCreate
            doc = DocumentService.create_document(db, DocumentCreate(
                title="Test Document",
                slug="test-doc",
                description="Testing document creation"
            ), owner_id=users[0].id)
            print(f"✓ Created document: {doc.title} (slug: {doc.slug})")
        
        db.close()
    except Exception as e:
        print(f"✗ Database operations failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    print("Testing both FastAPI applications...")
    
    agentic_ok = test_agentic_system()
    doc_ok = test_doc_api()
    
    print("\n=== SUMMARY ===")
    print(f"Agentic System Enhanced: {'✓ PASS' if agentic_ok else '✗ FAIL'}")
    print(f"Internal Documentation API: {'✓ PASS' if doc_ok else '✗ FAIL'}")
    
    if agentic_ok and doc_ok:
        print("\n✓ All tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed")
        sys.exit(1)
