import { Link } from "react-router-dom";

export default function Navbar() {
  // TODO: Render a top navigation bar with links to Dashboard and Transactions pages
  return (
    <nav>
      <Link to="/">Dashboard</Link>
      <Link to="/transactions">Transactions</Link>
      <Link to="/upload">Upload</Link>
    </nav>
  );
}
