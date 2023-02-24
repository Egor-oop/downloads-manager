import { Button, Container, Row, Col, InputGroup, Form, Alert } from 'react-bootstrap'
import React, { useState } from 'react'

function App() {
  const [mediaPath, setMediaPath] = useState('')
  const [documentsPath, setDocumentsPath] = useState('')
  const [isSuccess, setIsSuccess] = useState(false)

  const manageDownloads = () => {
    setIsSuccess(false)
    fetch('http://localhost:8000/manage/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify([
        {
          path: mediaPath,
        },
        {
          path: documentsPath,
        },
      ]),
    })
      .then((response) => response.json())
      .then((data) => {
        setIsSuccess(true)
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  return (

    <Container className='mt-2'>
      {isSuccess && (
        <Alert variant="success" onClose={() => setIsSuccess(false)} dismissible>
          Downloads folder has been managed <strong>successfully</strong>.
        </Alert>
      )}
      <div>
        <Form>
          <Row className="mb-4 mt-3">
            <Col>
              <InputGroup>
                <Form.Control
                  placeholder="path/to/media"
                  aria-label="Media path"
                  aria-describedby="basic-addon1"
                  onChange={(e) => setMediaPath(e.target.value) && console.log(mediaPath)}
                />
              </InputGroup>
            </Col>
            <Col>
              <InputGroup>
                <Form.Control
                  placeholder="path/to/documents"
                  aria-label="Documents path"
                  aria-describedby="basic-addon1"
                  onChange={(e) => setDocumentsPath(e.target.value) && console.log(documentsPath)}
                />
              </InputGroup>
            </Col>
          </Row>
          <Button
            variant="primary"
            onClick={() => manageDownloads()}
          >
            Manage
          </Button>
        </Form>
      </div>
    </Container>
  );
}

export default App;
