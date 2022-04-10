import React from "react";
import {Link} from 'react-router-dom';


const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td className="td">
                <Link to={`project/${project.name}`}>{project.name}</Link>
            </td>
            <td className="td">
                {project.githubUrl}
            </td>
            <td className="td">
                <ol>
                    {project.users.map((user,index) => <li key={index}>{user}</li>)}
                </ol>
            </td>
            <td>
                <button onClick={()=>deleteProject(project.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectsList = ({projects, deleteProject}) => {
    return (
        <div>
            <table>
                <th>
                    Project Name
                </th>
                <th>
                    URL
                </th>
                <th>
                    Users
                </th>
                <th></th>
                {projects.map((project, index) => <ProjectItem project={project} deleteProject={deleteProject}
                                                               key={index}/>)}
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectsList