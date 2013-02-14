class LoginController < ApplicationController

def create
	user = User.find_by_email(params[:email])

	if user && User.authenticate(user, params[:password])
		session[:user_id] = user.id
		redirect_to home_index_path
	else
		redirect_to :root
	end
end

def destroy

	session[:user_id] = nil
	redirect_to root_path

end


end
