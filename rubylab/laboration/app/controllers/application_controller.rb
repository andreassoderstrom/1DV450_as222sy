class ApplicationController < ActionController::Base
  protect_from_forgery

	def authenticate
		redirect_to :root unless session[:user_id]!= nil
	end
end
