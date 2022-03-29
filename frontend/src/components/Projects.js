import React from "react";
import {Link} from 'react-router-dom';


const ProjectItem = ({project}) => {
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
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
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
            {projects.map((project, index) => <ProjectItem project={project} key={index} />)}
        </table>
    )
}

export default ProjectsList