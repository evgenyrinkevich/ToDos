import axios from "axios";
import './App.css';
import React, {Fragment} from "react";
import UsersList from "./components/Users";
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
          'users': []
      }
  }

  componentDidMount() {
      axios.get('http://127.0.0.1:8000/api/users')
          .then(response => {
               const users = response.data
                 this.setState(
                     {
                         'users': users
                     }
                 )
          }).catch(error => console.log(error))
      }

    render() {
      return (
          <Fragment>
              <Menu />
              <UsersList users={this.state.users} />
              <Footer />
          </Fragment>
      )
  }
}

export default App;
