import React from 'react';
import './App.css';
import ReactDOM from 'react-dom';
import { Button, TextField } from '@mui/material';

class NameForm extends React.Component <any, any> {
  constructor(props: any) {
    super(props);
    this.state = {
      targets: 8,
      attackers: 13
    };

    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event: any) {
    this.setState({value: event.target.value});
  }

  render() {
    return (
      <form>
        <TextField id="outlined-basic" label="Number of targets:" variant="outlined" margin="normal" value={this.state.targets} onChange={this.handleChange}/>
        <br/>
        <TextField id="outlined-basic" label="Number of attackers:" variant="outlined" margin="normal" value={this.state.attackers} onChange={this.handleChange}/>
        <br/>
        <Button variant="contained" onClick={() => {alert(this.state.targets + ' targets and ' + this.state.attackers + ' attackers')}}>Submit</Button>
      </form>
    );
  }
}

ReactDOM.render(
  <NameForm />,
  document.getElementById('root')
);

export default NameForm;