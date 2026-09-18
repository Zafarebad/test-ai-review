// Simple user utility functions - has a few intentional issues
 
function getUser(id) {
    var user = users[id];  // bug: 'users' not defined anywhere
    return user;
}
 
function isAdmin(user) {
    if (user.role == "admin") {   // minor: should use === instead of ==
        return true
    }
}
 
function formatName(first, last) {
    return first + " " + last
}
 
// unused variable
let temp = 42;
 
module.exports = { getUser, isAdmin, formatName };