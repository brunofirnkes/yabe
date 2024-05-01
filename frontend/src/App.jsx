import react from 'react'
import { BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import ProtectedRoute from "./components/ProtectedRoute"
import Login from "./pages/Login"
import Home from "./pages/Home"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={
              <ProtectedRoute>
                <Home />
              </ProtectedRoute>}/>
        <Route path="/login" element={<Login />}/>
        <Route path="*" element={<Login />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
