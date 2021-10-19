import React from 'react';
import './App.css';
import ReactDOM from 'react-dom';
import { Button } from '@mui/material';

class NameForm extends React.Component <any, any> {
  constructor(props: any) {
    super(props);
    this.state = {
      targets: 8,
      attackers: 13
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event: any) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event: any) {
    alert(this.state.targets + ' targets and ' + this.state.attackers + ' attackers');
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Number of targets:
          <input type="text" value={this.state.targets} onChange={this.handleChange} />
        </label>
        <br/>
        <label>
          Number of attackers:
          <input type="text" value={this.state.attackers} onChange={this.handleChange} />
        </label>
        <br/>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

ReactDOM.render(
  <NameForm />,
  document.getElementById('root')
);

export default NameForm;