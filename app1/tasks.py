from app1.services.sync_rpc import SyncRpcClient
from app1.celery_app import app


@app.task(name="call_sync_notify_task")
def call_sync_notify_task():
    sync_rpc = SyncRpcClient()
    return sync_rpc.call()
