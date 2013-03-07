class ApplicationController < ActionController::Base
  protect_from_forgery

	def authenticate
		redirect_to :root unless session[:user_id]!= nil
	end

	def is_owner
		project = Project.find(params[:id])
		
		if project.owner_id != session[:user_id]
			redirect_to project_path(project.id)
		end

	end

	def is_member
		#är man en reggad användare av projektet
		project = Project.find(params[:id])
		
		project.users.each do |u|
			if u.id == session[:user_id]
				@bool = true;
			end
			
		end
		if @bool != true
			redirect_to projects_path
		end
	
	end



	def member_ticket
		#är man en reggad användare av projektet
		project = Project.find(params[:project_id])
		
		project.users.each do |u|
			if u.id == session[:user_id]
				@bool = true;
			end
			
		end
		if @bool != true
			redirect_to projects_path
		end
	
	end

	def is_ticket_owner
		ticket = Ticket.find(params[:id])
		project = Project.find(Ticket.find(params[:id]).project_id)

		if ticket.user_id != session[:user_id] # äger ticket
			if session[:user_id] != project.owner_id #äger projektet
				redirect_to project_ticket_path(project.id, ticket.id)
			end
		end


	end
end
