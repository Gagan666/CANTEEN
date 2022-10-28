import Button from '@mui/material/Button';
import { useHistory } from "react-router-dom";


export default function Home() {
    const history = useHistory();
    const signout = () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        history.push("/");
        document.location.reload();
    }
    return (
        <>
            <h1>Welcome</h1>

            <Button variant="outlined" onClick={signout}>Sign Out</Button>

        </>
    );
}