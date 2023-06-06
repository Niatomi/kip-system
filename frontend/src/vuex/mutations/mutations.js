export default {
    SET_ACCESS_TOKEN_TO_STATE: (state, token_data) => {
        state.accessHeader = {
            'Authorization': token_data.data.token_type + ' ' + token_data.data.access_token
        };
    },
};
