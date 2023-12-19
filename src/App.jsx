import React from 'react';

class App extends React.Component {
  startRelay = () => {
    fetch('http://localhost:5000/start')
      .then(response => response.text())
      .then(data => console.log(data), alert("Unlocked"))
      .catch(error => console.error('Error:', error));
  };

  stopRelay = () => {
    fetch('http://localhost:5000/stop')
      .then(response => response.text())
      .then(data => console.log(data), alert("Locked"))
      .catch(error => console.error('Error:', error));
  };

  render() {
    return (
      <div>
        <h1>Relay Control</h1>
        <button onClick={this.startRelay}>Start Relay</button>
        <button onClick={this.stopRelay}>Stop Relay</button>
      </div>
    );
  }
}

export default App;
