export function handleResponse(response) {
  return response.text().then(text => {
    const data = text && JSON.parse(text);
    if (!response.ok) {
      if (response.status === 401) {
        // auto logout if 401 response returned from api
        // location.reload()
      } else if (response.status === 400) {
        console.log(response.body);
      }
      const error = (data && data.message) || response.body;
      return Promise.reject(error);
    }
    return data;
  });
}
