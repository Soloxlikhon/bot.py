import redis

# Initialize Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Function to update payment status

def update_payment_status(payment_id, status):
    # Update the payment status in Redis
    redis_client.hset('payments', payment_id, status)
    
    # Fetch all admin message IDs related to payments
    admin_message_ids = redis_client.lrange('admin_messages', 0, -1)

    # Notify all admins about the payment status
    for message_id in admin_message_ids:
        notify_admin(message_id, payment_id, status)

# Function to simulate notifying an admin

def notify_admin(message_id, payment_id, status):
    print(f'Admin Notification: Payment ID {payment_id} status updated to {status} for message ID {message_id}')

# Integrate approve/reject payment system

# Example usage
# update_payment_status('PAY123', 'Approved')
