const form = document.getElementById('eventForm');
const submitBtn = document.getElementById('submitBtn');
const messageDiv = document.getElementById('message');

// Replace this with your actual API Gateway endpoint
const API_ENDPOINT =   "https://m492j306dc.execute-api.ap-south-1.amazonaws.com/prod/create-event";


form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form values
    const title = document.getElementById('title').value;
    const date = document.getElementById('date').value;
    const description = document.getElementById('description').value;

    // Prepare request body
    const requestBody = {
        title: title,
        date: date,
        description: description
    };

    // Disable submit button
    submitBtn.disabled = true;
    submitBtn.textContent = 'Submitting...';

    // Hide previous messages
    messageDiv.className = 'message';
    messageDiv.textContent = '';

    try {
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        if (response.ok) {
            // Success
            messageDiv.className = 'message success';
            messageDiv.textContent = 'Event created successfully!';
            form.reset();
        } else {
            // API returned an error
            const errorData = await response.json().catch(() => ({}));
            messageDiv.className = 'message error';
            messageDiv.textContent = errorData.message || `Error: ${response.status} - ${response.statusText}`;
        }
    } catch (error) {
        // Network or other error
        messageDiv.className = 'message error';
        messageDiv.textContent = `Failed to submit event: ${error.message}`;
    } finally {
        // Re-enable submit button
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit Event';
    }
});