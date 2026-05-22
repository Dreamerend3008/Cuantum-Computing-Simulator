export async function runSimulation(payload : object, API : string)
{
    const response = await fetch
    (
        `${API}/simulations/run`,
        {
            method : "POST",
            headers : {"Content-Type" : "application/json"},
            body : JSON.stringify(payload)
        }
    )
    const gate = await response.json()
    return gate
}