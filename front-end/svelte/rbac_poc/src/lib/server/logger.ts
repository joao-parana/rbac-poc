// FILE: src/lib/server/logger.ts
//
// Use this module only in +server.ts ou hooks.server.ts
// Import use the command below
// import { serverLogger } from '$lib/server/logger';
//
import { env } from '$env/dynamic/private';

export const serverLogger = {
	info: (message: string, data?: object) => {
		if (env.NODE_ENV !== 'production') {
			console.log(
				JSON.stringify({
					level: 'info',
					time: new Date().toISOString(),
					message,
					...data
				})
			);
		}
	},
	error: (error: unknown) => {
		console.error(
			JSON.stringify({
				level: 'error',
				time: new Date().toISOString(),
				error: error instanceof Error ? error.stack : String(error)
			})
		);
	}
};
