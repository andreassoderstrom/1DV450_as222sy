class ProjectsController < ApplicationController

def index
	@projects = Project.all
end

def show
	@project = Project.find(params[:id])
end

def new
	@project = Project.new
end

def create 
	@project = Project.new(params[:project])
	if @project.save
		redirect_to project_path(@project)
	else
		render :action => "new"
	end
end


 

end
