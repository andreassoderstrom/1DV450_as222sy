class ProjectsController < ApplicationController
before_filter :authenticate
def index
	@projects = Project.all
end

def show
	@users = Project.find(params[:id]).users
	@project = Project.find(params[:id])
	@tickets = Project.find(params[:id]).tickets
	session[:project_id] = params[:id]
end

def new
	@project = Project.new
	@users = User.all
end

def create 
	@project = Project.new(params[:project])
	@project.owner_id = session[:user_id]
	updateProjectUsers
	if @project.save
		redirect_to project_path(@project)
	else
		render :action => "new"
	end
end

def updateProjectUsers
		@project.users.delete(@project.users)
		
		params[:user_ids].each do |u|
			user = User.find(u)
			unless @project.users.include?(user)
				@project.users << user
			end
		end
end




def edit
	@users = User.all
	@project = Project.find(params[:id])
end

def update
		
		@project = Project.find(params[:id])
		updateProjectUsers
		if @project.update_attributes(params[:project])
			redirect_to project_path
		else
			render :action => "edit"
		end
end

def destroy
		@project = Project.find(params[:id])
		@project.destroy
		redirect_to projects_path
end


 

end
