import React, { useEffect, useState } from 'react';

const API_URL = 'https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/api/users';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setUsers(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title mb-4 text-warning">Users</h2>
          <table className="table table-hover table-bordered">
            <thead className="table-warning">
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Team</th>
                <th>Age</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={idx}>
                  <td>{user.name}</td>
                  <td>{user.email}</td>
                  <td>{user.team}</td>
                  <td>{user.age}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Users;
